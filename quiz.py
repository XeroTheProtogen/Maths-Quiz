from data_validation import force_float
from time import sleep
from math import ceil


def quiz():
  """The main function of the program & the sum of the functions within it"""
  # Play the intro
  intro()
  score, win_condition = questions()
  print(
    f"Score is {score}, and the minimum score needed to win is {win_condition}"
  )


def intro():
  print("""====================
  Welcome to the 2023 Math Quiz
  =========================""")
  print("""====================
  You'll be answering these three questions, 
  and if you get 67% of them correct, you win!
  =========================""")
  print("""====================
  Let's get started! Here is your first question...
  =========================""")
  sleep(6)


def questions():
  score = 0
  answer_one = force_float("""====================
  What is 5 + 7?
  =========================""")
  if answer_one == 12:
    print("""====================
    Correct!
    =========================""")
    score += 1
  else:
    print("""====================
    I am sorry, but that is incorrect. 
    The correct answer was 12
    =========================""")
  print("""====================
  Next question
  =========================""")
  answer_two = force_float("""====================
  What is 10 x 3?
  =========================""")
  if answer_two == 30:
    print("""====================
    Correct!
    =========================""")
    score += 1
  else:
    print("""====================
    I am sorry, but that is incorrect. 
    The correct answer was 30
    =========================""")
  answer_three = force_float("""====================
  What is 2^2?
  =========================""")
  if answer_three == 4:
    print("""====================
    Correct!
    =========================""")
    score += 1
  else:
    print("""====================
    I'm sorry, but that is incorrect
    The correct answer was 4
    =========================""")
  return score, ceil(3 / 2)
