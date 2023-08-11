# Questions and Answers are stored in this 2D arry
import random as rng  
  

def generate_questions(highest_number: int, number_of_questions: int, lowest_number=0,       decimals=False) -> list:
  questions=[]
  for i in range(number_of_questions):
    question = None
    answer = None
    a = None
    b = None
    if decimals == False:
      a = rng.randint(lowest_number, highest_number)
      b = rng.randint(lowest_number, highest_number)
    else: 
      a = round(rng.uniform(lowest_number, highest_number), 1)
      b = round(rng.uniform(lowest_number, highest_number), 1)
    operator = rng.randint(0, 3)
    if operator == 0:
      question = f"What is {a} + {b}"
      answer = round(a + b, 2)
    elif operator == 1:
      question = f"What is {a} - {b}"
      answer = round(a - b, 2)
    elif operator == 2:
      question = f"What is {a} / {b} (To the second decimal point, rounded up)"
      answer = round(a / b, 2)
    elif operator == 3:
      question = f"What is {a} x {b} (To the second decimal point, rounded up)"
      answer = round(a * b, 2)
    questions.append((question, answer))
  return questions


def pull_random_question(questions: list) -> tuple:
  if questions[0] == None:
    raise ValueError(f"No items can be found in list {questions}")

  q = rng.randint(0, len(questions - 1))
  return questions[q]


def ask_consequtive_questions(questions: list) -> tuple:
  for i in range(len(questions)):
    print(questions[i][0])
    print(questions[i][1])