import json
from difflib import get_close_matches

data=json.load(open("/home/sumit/PycharmProject/myapp/076 data.json"))
def transelater(w):
    w=w.lower()
    if w in data:
         return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn = input("did you mean %s instead? y for yes,n for no: " % get_close_matches(w,data.keys())[0])
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return "the word is doesn't exist"
    else:
        return "the word is doesn't exist please double check it"

word=input("the word: ")


output=transelater(word)


if type(output)==list:
    for item in output:
         print(item)
else:
    print(output)
