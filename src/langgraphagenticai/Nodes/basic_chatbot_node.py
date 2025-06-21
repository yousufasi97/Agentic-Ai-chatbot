
from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chat bot implementation
    """

    def __init__(self,model):
        self.llm = model

    def process(self,state:State)->dict:

        """
        Processess the input state and generates a chatbot response
        """

        return {"messages" :self.llm.invoke(state['messages'])}
