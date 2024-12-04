from football_stats.competitions import get_competitions, get_matches
from football_stats.matches import get_lineups, get_events, get_player_stats
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from tools.football import get_sport_specialist_comments_about_match as comments_about_a_match

import streamlit as st
import json

from agent import load_agent

msgs = StreamlitChatMessageHistory()


if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(messages=msgs, memory_key="chat_history", return_messages=True)

memory = st.session_state.memory

st.set_page_config(layout="wide",
                   page_title="Football Match Conversation App",
                   page_icon="⚽️")

# Utility functions
def reset_analysis():
    if "analysis" in st.session_state:
        del st.session_state["analysis"]

def load_competitions():
    """
    Simulates loading competitions from your function.
    Replace this with the actual call to fetch competitions.
    """
    return json.loads(get_competitions())

def load_matches(competition_id, season_id):
    """
    Simulates loading matches for a specific competition.
    Replace this with the actual call to fetch matches for a competition.
    """
    return  json.loads(get_matches(competition_id, season_id))

def start_conversation(match_id):
    """
    Simulates starting a conversation based on a match ID.
    Replace this with your custom logic to handle the conversation.
    """
    st.write(f"Starting conversation for match ID: {match_id}")

# Streamlit Sidebar
st.sidebar.title("Football Match Selector")
# Step 1: Select a Competition
selected_competition = None
selected_season = None
selected_match = None
match_id = None
match_details = None
specialist_comments = None

st.sidebar.header("Step 1: Select a Competition")
competitions = load_competitions()
competition_names = sorted(set([comp['competition_name'] for comp in competitions]))
selected_competition = st.sidebar.selectbox("Choose a Competition",
                                            competition_names,
                                            on_change=reset_analysis())
if selected_competition:
    # Step 2: Select a Season
    st.sidebar.header("Step 2: Select a Season")
    seasons = set(comp['season_name'] for comp in competitions
                  if comp['competition_name'] == selected_competition)
    selected_season = st.sidebar.selectbox("Choose a Season", sorted(seasons),
                                            on_change=reset_analysis())
    
    
if selected_season:
    # Get the selected competition ID
    competition_id = next(
        (comp['competition_id'] for comp in competitions 
         if comp['competition_name'] == selected_competition),
        None
    )
    season_id = next(
        (comp['season_id'] for comp in competitions 
                               if comp['season_name'] == selected_season 
                               and comp['competition_name'] == selected_competition),
        None
    )
    # Step 2: Select a Match
    st.sidebar.header("Step 3: Select a Match")
    matches = load_matches(competition_id, season_id)
    match_names = sorted([f"{match['home_team']} vs {match['away_team']}" for match in matches])
    
    if selected_match:=st.sidebar.selectbox("Choose a Match", match_names,
                                            on_change=reset_analysis()):
        # Get the selected match ID
        match_details = next(
            (match for match in matches if f"{match['home_team']} vs {match['away_team']}" == selected_match),
            None
        ) 
        match_id = match_details['match_id']
        
# Main Page
if not match_id:
    st.title("Football Match Conversation")
    st.write("Use the sidebar to select a competition, then a match, and start a conversation.")
else:
    st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True)
    st.markdown(f'<h1 class="title">{selected_match}</h1><h3 class="title">{selected_competition} - Season {selected_season}</h3>', unsafe_allow_html=True)

    col1, col2 = st.columns([0.4, 0.6])
    with col1:
        if 'analysis' not in st.session_state:
            with st.spinner("Specialist analysis in progress..."):
                specialist_comments = comments_about_a_match(
                    json.dumps(match_details), 
                    get_lineups(match_id)
                )
                st.session_state["analysis"] = specialist_comments
        with st.chat_message("specialist", avatar="👨🏼‍💼"):
            st.write(st.session_state["analysis"])
    with col2:
        st.write("Chat with the assistant")
          