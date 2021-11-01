# class of QuizBrain is created
class QuizBrain:
    def __init__(self, bank):
        self.question_number = 0
        self.score = 0
        # making question_bank the attribute whole question_bank is in question list
        self.question_list = bank

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # taking out the number of current question
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it Wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
