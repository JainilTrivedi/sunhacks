from t import EXAMPLES

t = []
for i in EXAMPLES:
    i["question"] = i["question"].replace("{", "{{").replace("}", "}}")
    i["answer"] =   i["answer"].replace("{", "{{").replace("}", "}}")

open('new.txt','w').write(str(EXAMPLES))
# code.replace("{", "{{").replace("}", "}}")