# importing all the necessary elements
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# empty list for saving question_data
question_bank = []


for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    # will initialize the Question class which has attributes and these parameters passed in it
    new_q = Question(question_text, question_answer)
    # appending the initialized data in empty list
    question_bank.append(new_q)

# object of QuizBrain
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've Completed the Quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")