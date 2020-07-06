import urllib.request
import json
import html
import random


class Trivia:
    def __init__(self):
        self.url = "https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple&"
        self.token = json.load(urllib.request.urlopen("https://opentdb.com/api_token.php?command=request"))
        self.open_url = urllib.request.urlopen(self.url + self.token["token"])
        self.data = json.load(self.open_url)

        for item in self.data["results"]:
            self.category = item["category"]
            self.question = item["question"]
            self.correct_answer = item["correct_answer"]
            self.incorrect_answers = item["incorrect_answers"]
            self.all_answers = item["incorrect_answers"]
            self.all_answers.insert(0, self.correct_answer)
            random.shuffle(self.all_answers)

    def return_category(self):
        return html.unescape(self.category)

    def return_question(self):
        return html.unescape(self.question)

    def return_correct_answer(self):
        return html.unescape(self.correct_answer)

    def return_incorrect_answers(self):
        return ", ".join(html.unescape(self.incorrect_answers))

    def return_all_answers(self):
        if len(self.all_answers) == 2:
            sorted_list = sorted(self.all_answers, reverse=True)
            return html.unescape(sorted_list)

        else:
            return html.unescape(self.all_answers)
