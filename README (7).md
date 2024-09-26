
# Negotiation Bot with Sentiment Analysis

## Overview
This project implements a negotiation bot using multimodal Large Language Models (LLMs) and the `Crewai` library. The bot processes user input to determine sentiment and negotiate product prices based on that sentiment. The system is built using `Gradio` for the user interface and leverages the `ChatGroq` model for natural language processing tasks.

## Components

### Agents
- **Sentiment Analyzer Agent**: This agent analyzes the sentiment of user messages (positive or negative) without revealing the sentiment to the user.
- **Negotiation Agent**: This agent negotiates the price of a product based on the sentiment passed from the Sentiment Analyzer Agent. Discounts are offered based on sentiment without explicitly mentioning it to the user.

### Crew
The system is organized using the `Crew` module which coordinates the agents to execute their tasks in sequence.

## Features
- Sentiment analysis of user input (positive/negative sentiment)
- Sentiment-based negotiation without explicitly disclosing sentiment
- Discounts based on sentiment score (positive sentiment leads to higher discounts)
- Gradio-based interface for user interaction

## Installation

1. Clone the repository.
2. Install dependencies using:
   ```bash
   pip install crewai gradio langchain_groq python-dotenv
   ```
3. Set up your `.env` file with the following variable:
   ```bash
   Groq_API_KEY=<your_api_key>
   ```

## Usage

1. Run the script using:
   ```bash
   python app.py
   ```
2. Open the local Gradio interface and interact with the negotiation bot. The bot will analyze your input and provide a price negotiation based on internal sentiment analysis.

## File Overview

- `app.py`: Main script that initializes agents, tasks, and the Gradio interface.
- `.env`: File for storing the API key for ChatGroq.

## Example
```bash
User input: "I really like the product, but it's too expensive."
Bot output: "We can offer you a 15% discount."
```

The bot analyzes the sentiment of the user message and negotiates a discount based on the sentiment.

## License
MIT License
