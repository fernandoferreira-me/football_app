from langchain.tools import tool
from langchain.chains import LLMChain
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def get_sport_specialist_comments_about_match(match_details: str, line_ups: str) -> str:
    """
    Returns the comments of a sports specialist about a specific match.
    The comments are generated based on match details and lineups.
    """
    
    agent_prompt = """
    You are a sports specialist with deep knowledge of football (soccer). 
    Your task is to analyze and explain the significance of a specific game 
    based on the details provided to you in JSON format. 
    
    
    Your response must include the following:
	1.	Game Overview:
		Explain the importance of the game (e.g., league match, knockout stage, rivalry, etc.).
		Specify when and where the game happened.
		Provide the result of the game.
	2.	Analysis of the Starting XI:
		Comment on the starting XI lineups for both teams.
		Identify key players and their potential roles in the match.
		Mention any notable absences or surprises in the lineup.
	3.	Contextual Insights:
		Offer insights into the broader context of the match 
        (e.g., historical rivalry, importance in the league standings, or notable storylines).
	4.	Tone of Response:
		Be professional, insightful, and engaging.
		Make the analysis clear and accessible to both casual fans and experts.
    
    The match details are provided by the json provided as follow: 
    {match_details}
    
    The team lineups are provided here:
    {lineups}
    
    Summary in 2 paragraphs. Em português, por favor.
    """
    llm = GoogleGenerativeAI(model="gemini-pro")
    input_variables={"match_details": match_details, "lineups": line_ups}
    prompt = PromptTemplate.from_template(agent_prompt)
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    
    return chain.run(
        **input_variables
    )