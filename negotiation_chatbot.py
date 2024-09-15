from crewai import Agent, Task, Crew, Process
import gradio as gr
from langchain_groq import ChatGroq
import os
import dotenv

dotenv.load_dotenv()

# present in .env
api_key = os.getenv("Groq_API_KEY")

llama_model = ChatGroq(
    api_key=api_key,
    model='llama3-groq-70b-8192-tool-use-preview'
)

sentiment_agent = Agent(
    role="Sentiment Analyzer",
    goal="""Analyze the sentiment of user messages to determine if they are positive or negative.
           Pass the sentiment information to the next agent without mentioning it in the response to the user.""",
    backstory="You are an AI assistant focused on analyzing sentiment for negotiation purposes, without revealing it to the user.",
    verbose=True,
    allow_delegation=False,
    llm=llama_model
)

negotiation_agent = Agent(
    role="Negotiation Agent",
    goal="""Negotiate a product price based on the initial price and sentiment score received internally. 
            If the sentiment is positive, offer a 10 to 20 percent discount; if negative, offer a 5 to 10 percent discount. 
            Never mention sentiment in the final response; just provide the counteroffer or price.""",
    backstory="""You negotiate prices based on the sentiment, 
              offering appropriate discounts and never ever mention the sentiment to the user in your output.
              make sure to remember the context of previous input by the user """,
    verbose=True,
    allow_delegation=False,
    llm=llama_model
)


def negotiate(user_message):
    initial_price = 100

    sentiment_analysis_task = Task(
        description=f"Analyze the sentiment of the user message: '{user_message}'",
        agent=sentiment_agent,
        expected_output="A sentiment score between -1 and 1 (this will be used internally)."
    )


    negotiation_task = Task(
        description=f"Negotiate based on the extracted price from the user message and the initial price '{initial_price}'. "
                    f"Provide a counter offer or acceptance of the price without mentioning the sentiment in the output.Never mention the sentiment of user in the input",
        agent=negotiation_agent,
        expected_output="A counter offer or acceptance of the price . Never mention about the sentiment of the user."
    )

    crew = Crew(
        agents=[sentiment_agent, negotiation_agent],
        tasks=[sentiment_analysis_task, negotiation_task],
        verbose=True,
        process=Process.sequential
    )

    output = crew.kickoff()
    return output.raw


iface = gr.Interface(
    fn=negotiate,
    inputs="text",
    outputs="text",
    title="Negotiation Bot",
    description="A bot that negotiates prices based on user input. Sentiment is considered internally but not revealed."
)

iface.launch()
