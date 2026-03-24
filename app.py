import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents import create_react_agent 
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/vr7/Desktop/Ollama/venv4/.env")

## Arxiv and Wikipedia Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
search = DuckDuckGoSearchRun(name="Search")

## Manual ReAct Prompt (no hub needed)
react_prompt = PromptTemplate.from_template("""Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}""")

st.title("🔎 LangChain - Chat with search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

## Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

if not api_key:
    st.warning("Please enter your Groq API Key in the sidebar to continue.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="What is machine learning?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.1-8b-instant", streaming=True)
        tools = [search, arxiv, wiki]

        agent = create_react_agent(llm, tools, react_prompt)
        search_agent = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            handle_parsing_errors=True
        )

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = search_agent.invoke(
                {"input": prompt},
                config={"callbacks": [st_cb]}
            )["output"]
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)

    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("💡 Make sure your Groq API Key is valid. Get one at https://console.groq.com")