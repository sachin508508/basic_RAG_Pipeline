from rag_pipeline import rag_chain
from exceptions import MissingAPIKeyException, MissingPDFFileException

print("""============================================================
📚 Welcome to the Basic RAG Pipeline
============================================================
Retrieve answers from your PDF using Retrieval-Augmented Generation.""")
try:
    while True:
        print(f"""{'-'*62}
    Available Options:
    1. Ask a question
    2. Exit
    {'-'*62}""")
        user_option = int(input("Enter your option (1 or 2): "))
        if user_option == 1:
            while True: 
                query = input("Enter the question: ").strip()
                if not query or len(query) < 10:
                    print("Please provide the prompt descriptively.")
                else:
                    chain = rag_chain()
                    response = chain.invoke(query)
                    print(f"Prompt: \n\t\t{query}\n\n{'-'*62}\n\nResponse: \n\t\t{response.text}\n\n{'-'*62}")
                    break
        elif user_option ==2:
            print("Quitting application!")
            break
        else:
            print("Incorrect input, press the correct number.")
            continue
except Exception as e:
    print(e)
#     pass
# chain = rag_chain()
# # query = "Which two organisations' AI-as-a-Service offerings increase the accessibility of AI technologies for the smaller businesses and non-technical users?"
# query = "who is the father of east india company?"
# response = chain.invoke(query)
# os.system("clear")
# print(response.text)