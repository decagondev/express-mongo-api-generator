from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import os

user_prompt_template = PromptTemplate(
    input_variables=["endpoints", "use_authentication"],
    template="""
Create a single-file Express.js application.

- Use **Express.js** as the framework.
- Use **Mongoose** for MongoDB.
- Include **Swagger UI** for API documentation.
- Enable **CORS** for all routes.
- Authentication: {use_authentication}
- Endpoints: {endpoints}

All the code should be in a single `.js` file with clear comments.
"""
)

llm = ChatOpenAI(temperature=0.5)

def create_express_app_chain(user_input: dict, output_file: str):
    chain = LLMChain(
        llm=llm,
        prompt=user_prompt_template,
        verbose=True  # For debugging/logging
    )

    generated_code = chain.run(user_input)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(generated_code)
    print(f"Application saved to {output_file}")

def express_app_repl():
    print("Welcome to the Express.js Application Generator!")
    print("Enter the details of the application you'd like to build:")

    endpoints = input("Endpoints (describe in detail): ")
    use_authentication = input("Use Authentication? (yes/no): ").lower() == "yes"

    user_input = {
        "endpoints": endpoints,
        "use_authentication": "Yes" if use_authentication else "No",
    }

    output_file = "express_app.js"

    create_express_app_chain(user_input, output_file)

if __name__ == "__main__":
    express_app_repl()
