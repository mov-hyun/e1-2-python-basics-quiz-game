class Quiz:
    # Quiz는 퀴즈 한 문제에 필요한 데이터와 동작만 담당한다.
    def __init__(self, question, choices, answer, hint=""):
        if len(choices) != 4:
            raise ValueError("choices must contain exactly 4 items.")
        if answer not in (1, 2, 3, 4):
            raise ValueError("answer must be a number from 1 to 4.")

        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def display(self):
        print(self.question)
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            hint=data.get("hint", ""),
        )
