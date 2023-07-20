import data_validation as data
from time import sleep
def quiz():
  print("""====================
  Welcome to the 2023 Math Quiz
  =========================""")
  sleep(3)
  print("""====================
  You'll be answering these three questions, 
  and if you get 67% of them correct, you win!
  =========================""")
  print("""====================
  Let's get started! Here is your first question...
  =========================""")
  answer_one = data.force_float("""====================
  What is 5 + 7?
  =========================""")
  if answer_one == 12:
    print("""====================
    Correct!
    =========================""")
  else:
    print("""====================
    I am sorry, but that is incorrect. 
    The correct answer was 12
    =========================""")
  print("""====================
  Next question
  =========================""")
  answer_two = data.force_float("""====================
  What is 10 x 3
  =========================""")
  if answer_two == 30:
    print("""====================
    Correct!
    =========================""")
  else:
    print("""====================
    I am sorry, but that is incorrect. 
    The correct answer was 30
    =========================""")