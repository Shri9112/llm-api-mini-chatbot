# LLM API Mini Chatbot

A beginner-friendly Python project for learning how to build an application around a Large Language Model (LLM) API.

This project uses the Gemini API and focuses on understanding the fundamental building blocks behind modern LLM applications: API communication, conversation history, structured output, temperature, streaming, and basic application architecture.

## Project Objective

The goal of this project is not just to build a chatbot, but to understand how an LLM-powered application works internally.

The project was built as a practical learning project before moving toward more advanced concepts such as:

- Embeddings
- Semantic Search
- Vector Databases
- Retrieval-Augmented Generation (RAG)
- Tool Calling
- Agentic AI
- Multilingual NLP
- Trust and Verification

## Features

### 1. Gemini API Integration

Connects a Python application to the Gemini API and sends prompts to an LLM.

### 2. Conversation History

The application maintains conversation history during the current program session.

Instead of sending only the latest user message, previous messages are included as context for the next request.

### 3. Temperature Experiment

The project includes an experiment to observe how different temperature values affect model output.

Tested values include:

- 0.0
- 0.5
- 1.0
- 1.5

### 4. Structured Output

The project experiments with requesting JSON-formatted responses from the LLM and parsing them using Python's json module.

Concept:

LLM Response
    |
    v
JSON string
    |
    v
json.loads()
    |
    v
Python dictionary

### 5. Streaming Responses

The project uses Gemini's streaming API to receive generated content in chunks instead of waiting for the complete response.

Concept:

Gemini API
    |
    v
Chunk 1
Chunk 2
Chunk 3
Chunk 4
    |
    v
Display progressively

The complete response is then stored in the conversation history.

### 6. Clear Conversation

The chatbot provides a command to clear the current conversation history.

Command:

clear

### 7. Exit

The chatbot can be closed using:

exit

## Concepts Learned

This project was used to understand the following concepts practically:

- LLM API request/response flow
- API keys and environment variables
- .env files
- .gitignore
- Conversation history
- Application state
- Stateless API requests
- Prompt construction
- Temperature
- JSON and Python dictionaries
- json.loads()
- Streaming responses
- Streaming chunks
- API errors and quota limitations
- Python modules
- Separation of concerns
- Basic project architecture

## Project Architecture

The project separates different responsibilities into different modules.

                    User
                      |
                      v
                  main.py
                      |
                      v
                   chat.py
                      |
             +--------+--------+
             |                 |
             v                 v
     conversation.py      llm_client.py
             |                 |
             |                 v
             |             Gemini API
             |                 |
             +--------+--------+
                      |
                      v
                  Response
                      |
                      v
               Update History
                      |
                      v
                  User Output

### Module Responsibilities

#### config.py

Loads environment variables and stores configuration such as the Gemini API key and model name.

#### llm_client.py

Handles communication with the Gemini API.

#### conversation.py

Manages conversation history and constructs the context sent to the model.

#### chat.py

Coordinates conversation management and LLM interaction.

#### main.py

Acts as the entry point and handles the interactive command-line interface.

## Project Structure

llm-api-mini-chatbot/
|
├── .env
├── .gitignore
├── README.md
├── requirements.txt
|
├── data/
│   └── conversations/
|
├── experiments/
│   ├── 01_basic_api.py
│   ├── 02_conversation.py
│   ├── 02b_conversation_with_history.py
│   ├── 03_temperature.py
│   ├── 04_structured_output.py
│   └── 05_streaming.py
|
└── src/
    ├── __init__.py
    ├── config.py
    ├── llm_client.py
    ├── conversation.py
    ├── chat.py
    └── main.py

## Experiments

The experiments/ directory contains small experiments used to understand individual concepts before integrating them into the final chatbot.

### 01_basic_api.py

Basic Gemini API request and response.

### 02_conversation.py

Initial interactive chatbot loop.

### 02b_conversation_with_history.py

Manual conversation history implementation.

### 03_temperature.py

Experimenting with different temperature values.

### 04_structured_output.py

Experimenting with structured JSON output and JSON parsing.

### 05_streaming.py

Experimenting with streaming responses.

## Requirements

- Python 3.x
- Gemini API key
- google-genai
- python-dotenv

## Setup

### 1. Clone the repository

git clone https://github.com/Shri9112/llm-api-mini-chatbot.git

Move into the project:

cd llm-api-mini-chatbot

### 2. Create a virtual environment

python -m venv .venv

Activate it on macOS/Linux:

source .venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Create the environment file

Create a file named:

.env

Add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

The .env file is intentionally excluded from Git using .gitignore.

Never commit API keys or other secrets to GitHub.

## Run the Chatbot

From the project root:

cd src
python main.py

The chatbot provides an interactive terminal interface.

#Example:

================================
      LLM Mini Chatbot
================================
Type 'exit' to quit.
Type 'clear' to clear conversation.

You: My favourite colour is blue
AI: ...

You: What is my favourite colour?
AI: Your favourite colour is blue!

You: clear
Conversation cleared.

You: What is my favourite colour?
AI: I don't know your favorite colour yet.

## Security

The Gemini API key is stored in an environment variable instead of being written directly into the source code.

The .env file is excluded from Git using .gitignore.

Before pushing a project to GitHub, always verify that secrets are not being tracked.

## Future Learning Path

This project is the first step toward building more advanced LLM and NLP systems.

The planned learning progression is:

LLM API
   |
   v
Embeddings
   |
   v
Semantic Search
   |
   v
Vector Database
   |
   v
RAG
   |
   v
Tool Calling
   |
   v
Agents
   |
   v
Multilingual RAG
   |
   v
Trust and Verification
   |
   v
Research Project

The next project will focus on embeddings and semantic search.

## Learning Philosophy

The project is intentionally built step-by-step instead of immediately using large frameworks.

The objective is to understand the underlying concepts first and introduce frameworks only after the fundamentals are clear.

## Author

Shri

B.Tech - Computer Science and Data Science

This repository is part of a practical learning journey toward Large Language Models, NLP, RAG, Agentic AI, and trustworthy AI systems.
