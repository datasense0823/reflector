# 2 Chain: 1. Generate 2. Reflect Chain

# Create Generate Chain

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_groq import ChatGroq

llm=ChatGroq(temperature=0,model="llama3-70b-8192")

generation_prompt=ChatPromptTemplate.from_messages(
    [("system","You are an Editor in a new company. Write a 50 words article based on user question"),
     MessagesPlaceholder(variable_name="messages")

    ]
)


reflection_prompt=ChatPromptTemplate.from_messages(
    [("system","You are a Critic. Generate critique and recommendations for the user's Article. Always provide detailed recommendations, including requests for length, virality, style, etc "),
     MessagesPlaceholder(variable_name="messages")
    ]
)


generate_chain= generation_prompt | llm

reflection_chain=reflection_prompt | llm








