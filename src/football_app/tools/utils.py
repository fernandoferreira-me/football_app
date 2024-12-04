
from langchain.utilities import GoogleSerperAPIWrapper


def get_search_utility():
    SERPER_API_KEY = "644ebf22af0886314c0aaf6a28fa085a25529bfc" # replace with your own key
    search = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)
    return search