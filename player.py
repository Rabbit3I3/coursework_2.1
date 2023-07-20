class Player:
    def __init__(self, name):
        self.name = name
        self.answers = []


    def check_answers(self, answer):
        return answer in self.answers

    def add_answers(self, answer):
        self.answers.append(answer)

    def count_answers(self):
        return len(self.answers)

    def __repr__(self):
        return self.name, self.answers


