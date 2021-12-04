import urllib.request as ur
import json

gameid = input("Enter game id: ")
url = "https://play.kahoot.it/rest/kahoots/" + gameid
q = json.loads(ur.urlopen(url).read())["questions"]
four_list = ["red", "blue", "yellow", "green"]
two_list = ["blue", "red"]

for index, slide in enumerate(q):
    if slide.get("type") == "quiz":
        for i in range(len(slide.get("choices"))):
            if slide["choices"][i]["correct"]:
                if(len(slide.get("choices")) == 2):
                    colours_list = two_list
                else:
                    colours_list = four_list
                print("Question number: {}\n{}\n{}\n".format(
                    index + 1, slide["choices"][i].get("answer"), colours_list[i]))
