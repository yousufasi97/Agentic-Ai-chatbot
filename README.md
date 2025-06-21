### End to End Agnetic AI RAG Chatbot



Streamlit app with three modes:

* Basic chat  
* Web-augmented chat (retrieval-augmented via Tavily)  
* AI news digests (daily / weekly / monthly)

All modes use Groq LLM and are wired with LangGraph/LangChain.

---

## Quick start

```bash
git clone https://github.com/yousufasi97/Agentic-Ai-chatbot.git
cd Agentic-Ai-chatbot

create a virutal environment using python3.13 



# Install the requirement by running

pip install -r requirements.txt

# API keys
export GROQ_API_KEY="sk-..."     # required
export TAVILY_API_KEY="tv-..."   # needed for web/news modes

streamlit run app.py
