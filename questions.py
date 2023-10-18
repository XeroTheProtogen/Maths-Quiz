# Questions and Answers are stored in this 2D arry
import random as rng
import debug

def generate_questions(subtraction:bool, multiplication:bool, division:bool) -> list:
  """The function which generates the questions of the quiz, 
  it uses a series of boolean variables to generate specific types of questions.
  Can only generate 10 questions at a time"""
  #Initialize question list
  questions = []
  print((subtraction, multiplication, division))
  #Run generation loop
  for i in range(10):
    #Initialize question and answer
    question = None
    answer = None
    #Variables for questions
    a = rng.randint(1, 10)
    b = rng.randint(1, 10)
    #The operator variable is a random integer used to determine which type of math question is generated.
    #The types of questions generated are determined by the booleans in function parameters
    operator = operator_range(subtraction, multiplication, division)

    #Select the type of question generated: 0 = addition, 1 = subtraction, 2 = multiplication, 3 = division
    if operator == 0:
      question = f"What is {a} + {b}? "
      answer = round(a + b, 2)
    if operator == 1:
      question = f"What is {a} - {b}? "
      answer = round(a - b, 2)
    if operator == 2:
      question = f"What is {a} x {b}? "
      answer = round(a * b, 2)
    if operator == 3:
      question = f"What is {a} / {b} \n(rounded to the second decimal, if needed)? "
      answer = round(a / b, 2)
    #Add the question and answer generated to the questions list as a tuple (More data efficient)
    questions.append((question, answer))
  #Once the generation loop ends, return the filled questions list
  return questions


def operator_range(sub, mul, div):
  """Due to the nature of variable mutability, 
  randomizing the operator had to be moved into a separate function."""
  #The logic is difficulty based, where subtraction is easier than multiplication,
  #and multiplication is easier than division.
  #Initialize operator
  operator = 0
  if sub:
    operator = rng.randint(0, 1)
    if mul:
      operator = rng.randint(0,2)
      if div:
        operator = rng.randint(0,3)
        return operator
      else:
        return operator
    else:
      return operator
  else:
    return 0


def ask_consequtive_questions(questions: list) -> int:
  """Goes through each question and asks the player for the answer.
  Also handles tracking points earned"""
  #Initialize points
  points = 0
  #Run through each question via a for loop
  for i in range(len(questions)):
    #Ask the player for the answer to the question
    answer = debug.force_float(questions[i][0])
    #Determine if the answer provided is correct
    if answer == questions[i][1]:
      print("Correct!")
      #If so, give the player a point
      points += 1
    elif answer != questions[i][1]:
      print(f"Incorrect, the answer was {questions[i][1]}")
  print(points)
  return points