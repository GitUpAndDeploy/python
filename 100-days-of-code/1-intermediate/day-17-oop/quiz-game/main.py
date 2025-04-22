from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range (len(question_data)):
  question_text = question_data[i]["text"] 
  question_answer = question_data[i]["answer"]
  new_qestion = Question(question_text, question_answer)
  question_bank.append(new_qestion)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")
