#April 22.2025

from typing import List,Sequence
import os
from state import State #Importing State Class
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage,HumanMessage,AIMessage
from langgraph.graph import START,END,MessageGraph
from chains import generate_chain,reflection_chain
from langgraph.graph import StateGraph
load_dotenv()

# def generate_node(state:Sequence[BaseMessage])-> List[BaseMessage]:
#     response=generate_chain.invoke({"messages":state})
#     return response.content

# def reflection_node(state:Sequence[BaseMessage])-> List[BaseMessage]:
#     response=generate_chain.invoke({"messages":state})
#     return HumanMessage(content=response.content)


#Generate Node-Function
#Take User Input and Generate 

def generate_node(input:State)->State:
    question=input["question"]
    response=generate_chain.invoke({"messages":question})
    answer=response.content
    return {"generation":answer}

def reflection_node(input:State)->State:
    question=input["generation"][-1]
    response=reflection_chain.invoke({"messages":question})
    answer=HumanMessage(content=response.content)
    return {"reflection":answer}

#Giving Name to the nodes

Generate="Generate"
Reflect="Reflect"

#Initializing Graph (Blank Graph)

graph_builder = StateGraph(State)

#Create Nodes

graph_builder.add_node(Generate,generate_node)
graph_builder.add_node(Reflect,reflection_node)
graph_builder.set_entry_point(Generate)

def should_continue(input:State):
    generation=input["generation"]
    if len(generation)>3:
        return END
    return Reflect

#Create Edges

graph_builder.add_conditional_edges(Generate,should_continue)
graph_builder.add_edge(Reflect,Generate)

graph=graph_builder.compile()

graph.get_graph().draw_mermaid_png(output_file_path="graph.png")

if __name__== "__main__":
    input={"question":"Explain me XG Boost" ,"generation":[],"reflection":""}
    response=graph.invoke(input)










