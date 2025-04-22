# TODO: Asking the questions
# TODO: Check if the answer was correct
# TODO: Check if there are still questions left

class QuizBrain:
  def __init__(self, question_list):
    """Initializes the quiz with a list of questions."""
    self.question_number = 0
    self.score = 0
    self.question_list = question_list

  def next_question(self):
    """Returns the next question in the quiz."""
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
    self.check_answer(user_answer, current_question.answer)
  
  def still_has_questions(self):
    """Checks if there are still questions left in the quiz."""
    return self.question_number < len(self.question_list)
  
  # Checking the answer
  def check_answer(self, user_answer, correct_answer):
    """Checks if the user's answer is correct."""
    current_question = self.question_list[self.question_number - 1]
    if user_answer.lower() == correct_answer.lower():
      print("You got it right!")
      self.score += 1
      # return True
    else:
      print("That's wrong.")
      # return False
    print(f"The correct answer was: {correct_answer}")
    print(f"Your current score is: {self.score}/{self.question_number}")
    print("\n")
