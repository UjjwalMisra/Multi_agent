import streamlit as st
import os
from pydantic import BaseModel
from typing import Optional, Type
from langchain_community.llms import Ollama  # Local LLM
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.tools import BaseTool
from langchain.memory import ConversationBufferMemory
from langchain_community.utilities import SerpAPIWrapper
from langchain_core.messages import HumanMessage, AIMessage

# Initialize Streamlit session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Streamlit UI
st.title("AI/GenAI Use Case Generation System")

# Model selection
llm_type = st.radio("Select LLM type:", ["Local (Ollama)", "Cloud (OpenAI)"])

if llm_type == "Cloud (OpenAI)":
    if 'OPENAI_API_KEY' not in st.secrets:
        st.error("OpenAI API key missing in secrets.toml")
        st.stop()
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Search tool setup
if "SERPAPI_API_KEY" in st.secrets:
    os.environ["SERPAPI_API_KEY"] = st.secrets["SERPAPI_API_KEY"]
search = SerpAPIWrapper()

class SearchArgs(BaseModel):
    query: str

class DatasetSearchTool(BaseTool):
    name: str = "dataset_search"
    description: str = "Searches for datasets"
    args_schema: Optional[Type[BaseModel]] = SearchArgs
    
    def _run(self, query: str) -> str:
        return f"Searching for datasets related to: {query}"
    
    def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not implemented")

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for searching information"
    ),
    DatasetSearchTool(),
]

# Display chat history
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# Input form
input_type = st.radio("Select research target:", ["Company", "Industry"])
company_name = st.text_input("Enter company name:") if input_type == "Company" else None
industry = st.text_input("Enter industry:") if input_type == "Industry" else None

if llm_type == "Local (Ollama)":
    ollama_model = st.selectbox(
        "Select Ollama model:",
        ["llama3", "mistral", "phi3", "gemma:2b"]
    )
    temperature = st.slider("Temperature:", 0.0, 1.0, 0.7)
else:
    model = st.selectbox("Select OpenAI model:", ["gpt-4", "gpt-3.5-turbo"])
    temperature = st.slider("Temperature:", 0.0, 1.0, 0.7)

if st.button("Generate Use Cases") and (company_name or industry):
    with st.spinner("Generating AI use cases..."):
        try:
            # Initialize LLM
            if llm_type == "Local (Ollama)":
                llm = Ollama(
                    model=ollama_model,
                    temperature=temperature
                )
            else:
                from langchain_openai import ChatOpenAI
                llm = ChatOpenAI(
                    model=model,
                    temperature=temperature
                )
            
            memory = ConversationBufferMemory(
                memory_key="chat_history",
                return_messages=True
            )
            
            agent = initialize_agent(
                tools, 
                llm, 
                agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
                memory=memory,
                handle_parsing_errors=True
            )
            
            query_text = f"Research {company_name if company_name else industry}"
            result = agent.invoke({"input": query_text})
            
            st.session_state.chat_history.extend([
                HumanMessage(content=query_text),
                AIMessage(content=result["output"])
            ])
            
            # Display and download results
            st.subheader("Research Results:")
            st.write(result["output"])
            
            st.download_button(
                label="Download Report",
                data=result["output"],
                file_name="ai_use_cases.md"
            )
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            if "Ollama" in str(e):
                st.info("Make sure Ollama is running: `ollama serve`")
else:
    st.warning("Please provide either a company name or an industry.")