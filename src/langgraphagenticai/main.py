import streamlit as st

from src.langgraphagenticai.Ui.streamlit.display_result import DisplayResultsStreamlit
from src.langgraphagenticai.Ui.streamlit.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
def load_langraph_agencticai_app():
    """
    Load and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness
    
    
    """

    ##Load UI
    ui = LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    #Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:

        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # Configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM Model could not be initialized.")
                return
            
            # Initilaze and set up the graph based on use case
            usecase =  user_input.get("selected_usecases")
            if not usecase:
                st.error("Error: No use case selected.")
                return
            
            ### building Graph
            graph_builder = GraphBuilder(model)

            try:
                graph=graph_builder.setup_graph(usecase)
                print(user_message)
                DisplayResultsStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph set up failed- {e}")
                return
            
        except Exception as e:
            st.error(f"Error: Graph set up failed- {e}")
            return