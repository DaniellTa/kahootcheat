import urllib.request as ur
import json

gameid = input("Enter game id: ")
url = "https://play.kahoot.it/rest/kahoots/" + gameid

s = ur.urlopen(url)
sl = s.read()
d = json.loads(sl)
q = d["questions"]

colours_list = ["red", "blue", "yellow", "green"]
for index, slide in enumerate(q):
    if slide.get("type") == "quiz":
        for i in range(len(slide.get("choices"))):
            if slide["choices"][i]["correct"] == True:
                print("Question number: {}\n{}\n{}\n".format(
                    index + 1, slide["choices"][i].get("answer"), colours_list[i]))
