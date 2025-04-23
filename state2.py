from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

class State(TypedDict):
    question: str
    generation: Annotated[list, add_messages]
    reflection: str


# graph_builder = StateGraph(State)


