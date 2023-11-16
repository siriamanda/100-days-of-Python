from question_model import Question            # From question_model file import the Question class
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:                          # loop through the list of questions in the data file
    question_text = question["text"]                    # save each question and answer in two variables
    question_answer = question["answer"]
    new_q = Question(question_text, question_answer)    # create an object for each question
    question_bank.append(new_q)                         # save each object to the question_bank list

quiz = QuizBrain(question_bank)                         # create object from class QuizBrain

while quiz.still_has_questions():
    quiz.next_question()                                  # call the method next_question from the object

quiz.final_score()
