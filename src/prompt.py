from langchain_core.prompts import ChatPromptTemplate

system_prompt = "You are an helpful assistant. Answer the query strictly using the provided context. "\
"Rules:"\
"1. Rely only on clear facts in the context. Do not extrapolate or use outside knowledge."\
"2. If the context lacks the answer, state: 'Information not found in documents.'"\
"3. Be direct and concise."\
"Context: {context}"
user_prompt = "{query}"
def get_message():
    return ChatPromptTemplate.from_messages([
        ("system",system_prompt),
        ("human", user_prompt)
    ])


