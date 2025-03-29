import requests

code = open('code.txt','r').read()

post = requests.post('http://localhost:5000/generate_mermaid_chart', json={'code': code, 'daiagram': 'flowchart'})

print(post.json())