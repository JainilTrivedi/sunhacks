from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.prompts.few_shot import FewShotPromptTemplate
import flask
from dotenv import load_dotenv


from constants import EXAMPLES

for i in EXAMPLES:
    i["question"] = i["question"].replace("{", "{{").replace("}", "}}")
    i["answer"] =   i["answer"].replace("{", "{{").replace("}", "}}")


tests = [
"""
import threading


def print_cube(num):
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    print("Square: {}" .format(num * num))


if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
    """    
]


load_dotenv()

class LLM:
    def __init__(self):
        self.llm =  OllamaLLM(model="llama3")
        # self.llm = ChatOpenAI(api_key='sk-proj-gCFNquhpCLeiwKC2qPTyT3BlbkFJ4x0wIGtHpV1pEIBj2FO3')
    def generate_mermaid_chart(self,diagram,code):
        print(type(llm))
        examples = EXAMPLES

        example_prompt = PromptTemplate.from_template( "question: {question}\nanswer: {answer}")
        
        # print(example_prompt.format(**EXAMPLES[0]))
        

        prefix = "Here are some examples of generating different types of mermaid scripts for code given to us:\n"
        suffix = "\nQuestion: {input}"

        # Create the FewShotPromptTemplate
        few_shot_prompt = FewShotPromptTemplate(
            examples=examples,
            example_prompt=example_prompt,
            # prefix=prefix,
            suffix=suffix,
            input_variables=["input"]
        )
        # print(f'What is mermaid script to generate {diagram} for the code\n{code}')

        # print(few_shot_prompt.invoke( {"input" : """What is mermaid script to generate {diagram}for the code\n{code}""" }  ))

        new_input = { "input" : """Generate mermaid script showing {diagram} for the code\n""" + code }
        formatted_prompt = few_shot_prompt.format(input=new_input)
        # print(formatted_prompt)
        # formatted_prompt = few_shot_prompt.format(**new_input).to_string()

        reply = self.llm.invoke(formatted_prompt)
        return reply
        # return reply.content
    



llm = LLM()

code = open('code.txt','r').read()
# script = llm.generate_mermaid_chart("flowchart",tests[0])


# print(script)

app = flask.Flask(__name__)

@app.route('/')
def index():
    json = {
        'code': "graph TD:A[Start] --> B{Is it working?}; B -- Yes --> C[Hello World!]; B -- No --> D[Check the script]; D --> B;" }
    return json

"""generate psudo code"""
# @app.route('/generate_psudo_code', methods=['POST'])
# def generate_psudo_code():
#     data = flask.request.json
#     code = data['code']
#     llm = LLM()
#     response = llm.generate_psudo_code(code)
#     json ={
#         'code': response
#     }
#     return json

# generate_mermaid_chart
@app.route('/generate_mermaid_chart', methods=['POST'])
def generate_mermaid_chart():
    data = flask.request.json
    code = data['code']
    daiagram = data['daiagram']
    llm = LLM()
    response = llm.generate_mermaid_chart(code,daiagram)
    json ={
        'code': response
    }
    return json


if __name__ == '__main__':
    app.run(debug=True)









