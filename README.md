# AI Use Case Generation System

A multi-agent system that generates AI/GenAI use case proposals for companies or industries, supporting both cloud-based (OpenAI) and local (Ollama) LLMs.

![image](https://github.com/user-attachments/assets/4ba135d5-1781-45d2-8880-7da632c4075c)
![image](https://github.com/user-attachments/assets/bf92450a-da72-4365-ba09-045e866835d5)

![image](https://github.com/user-attachments/assets/a7251d32-d712-4754-b47b-65cd573ed10b)
![image](https://github.com/user-attachments/assets/d649e5a2-df0d-4923-beb6-4ddccd17382b)



## Features

- **Dual LLM Support**: Choose between OpenAI's GPT models or local Ollama models
- **Multi-Agent Architecture**: Specialized agents for research, analysis, and proposal generation
- **Conversational Memory**: Maintains context throughout the session
- **Web Search Integration**: Augments responses with live web data
- **Markdown Export**: Download generated proposals in markdown format

## Prerequisites

- Python 3.10+
- Ollama (for local LLMs) - [Installation Guide](https://ollama.com/)
- API keys (for cloud services)

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/multi-agent-ai.git
cd multi-agent-ai
Install dependencies:



pip install -r requirements.txt
Set up environment:


cp .env.example .env
# Edit .env with your API keys
Configuration
For Ollama (Local LLMs)

ollama pull llama3  # Or any supported model
For OpenAI
Add your API key to .streamlit/secrets.toml:

toml

OPENAI_API_KEY = "your-api-key"
SERPAPI_API_KEY = "your-serpapi-key"  # Optional for web search
Usage

streamlit run app.py
Command Line Version

python main.py --company "Apple"  # Or --industry "Healthcare"
System Architecture
mermaid

graph TD
    A[User Input] --> B(Industry Research Agent)
    A --> C(Market Standards Agent)
    B --> D(Use Case Generator)
    C --> D
    D --> E(Resource Collector)
    E --> F(Proposal Synthesizer)
    F --> G[Markdown Output]
Supported Models
Model Type	Options
OpenAI	gpt-4, gpt-3.5-turbo
Ollama	llama3, mistral, phi3, gemma:2b

Contributing
Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

License
Distributed under the MIT License. See LICENSE for more information.


Project Link: https://github.com/yourusername/Multi_agent
