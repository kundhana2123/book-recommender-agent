# Book Recommender Agent

This project is an interactive Book Recommender Agent built using the **LangGraph ReAct Agent framework**, enhanced with **LangChain** tools and **Judgeval** for tracing and evaluation.<br>

The agent takes user input on book preferences (e.g., "mystery novels") and uses the **Google Books API** to recommend top matching books. It also integrates with **Judgeval** to log and evaluate the conversation flow for improvement and observability.<br>

## Features

- Built using **LangGraph**'s `create_react_agent` prebuilt ReAct agent.<br>
- Uses a **tool** to search for books via the **Google Books API**.<br>
- Integrates **Judgeval** for tracing and quality evaluation.<br>
- Interactive command-line interface.<br>
- Handles API failures gracefully.<br>

## Getting Started
### 1. Clone the repository

git clone https://github.com/yourusername/book-recommender-agent.git <br>
cd book-recommender-agent <br>

### 2. Create a virtual environment
python -m venv venv <br>
source venv/bin/activate <br> 

### 3. Install dependencies
pip install -r requirements.txt <br>

### 4. Set up environment variables
Create a .env file with your OpenAI and Judgeval API keys: <br>
OPENAI_API_KEY=your_openai_key <br>
JUDGMENT_API_KEY=your_judgeval_key <br>
JUDGMENT_ORG_ID=your_judgeval_org_id <br>

### How It Works
The user is prompted to enter the type of books they’re looking for. <br>
The agent uses an LLM (gpt-3.5-turbo) to interpret the input and call a search_books_tool. <br>
The tool queries the Google Books API to fetch relevant books. <br>
The final recommendations are displayed in a readable format. <br>
Judgeval traces the interaction and scores output relevance for observability and debugging. <br>
![img](https://file%252B.vscode-resource.vscode-cdn.net/Users/kundhana_hp/Downloads/book-recommender-agent/architecture.png?version%253D1752444710589)

## Example Output
Welcome to the Book Recommender Agent! <br>
What type of books are you looking for? (e.g., mystery novels): mystery <br>
Recommended Books: <br>

I found some mystery books for you: <br>

1. "The Mystery Book Mystery" by Wylly Folk St. John <br>
2. "The Mystery Readers' Advisory" by John Charles, Joanna Morrison, and Candace Clark <br>
3. "Crime & Mystery" by Henry Reymond Fitzwalter Keating <br>

Would you like more information about any of these books?<br>

## Evaluation & Tracing
This agent is fully instrumented using Judgeval, which provides:<br>
- Span tracing for each step (input, tool calls, outputs)<br>
- Live monitoring<br>
- Evaluation scoring with AnswerRelevancyScorer<br>