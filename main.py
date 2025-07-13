import os
import requests
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from judgeval.common.tracer import Tracer
from judgeval.integrations.langgraph import JudgevalCallbackHandler
from judgeval.scorers import AnswerRelevancyScorer

load_dotenv()

tracer = Tracer(
    api_key=os.getenv("JUDGMENT_API_KEY"),
    project_name="react-book-agent",
    enable_monitoring=True
)
handler = JudgevalCallbackHandler(tracer)

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

@tool
def search_books_tool(query: str) -> str:
    """Search books via Google Books API based on a query string."""
    try:
        response = requests.get(
            "https://www.googleapis.com/books/v1/volumes",
            params={"q": query, "maxResults": 3}
        )
        response.raise_for_status()
        items = response.json().get("items", [])
        if not items:
            return "No books found for your query."
        return "\n".join(
            f"{book['volumeInfo'].get('title', 'Unknown Title')} — {', '.join(book['volumeInfo'].get('authors', ['Unknown Author']))}"
            for book in items
        )
    except Exception as e:
        return f"Error occurred while fetching books: {e}"

agent = create_react_agent(
    model=model,
    tools=[search_books_tool],
    prompt="You are a book-savvy assistant that asks clarifying questions, searches via the tool, and recommends books.",
    response_format=None,
    debug=True
)

def run():
    print("Welcome to the Book Recommender Agent!")
    user_input = input("What type of books are you looking for? (e.g., mystery novels): ").strip()

    state = {
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    result = agent.invoke(state, config={"callbacks": [handler]})

    print("\nRecommended Books:\n")
    print(result["messages"][-1].content)

if __name__ == "__main__":
    run()
