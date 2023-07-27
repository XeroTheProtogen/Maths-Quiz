# Questions and Answers are stored in this dictionary
# The branching in this dictionary works as so:
# Master dictionary -> branching dictionaries containing questions and answers -> Question and Answer
# This is temporary though, since a tree system might be better for this purpose
import tree

''' {
  "question_1": {
    "question": "What is 1 + 1",
    "answer": ["2", "two"]
  },
  "question_2": {
    "question": "What is 5 x 5",
    "answer": "25"
  }
'''


def retrieve_question_and_answer(question_number: int):
  # Use the Guard pattern to check if the provided integer has a corresponding question
  if question_number > len(questions) + 1 or question_number < 1:
    raise ValueError(f"Error: No 'Question {question_number}' can be found")

  # Retrieve question and answer from dictionary
  question = questions[f"question_{question_number}"]

  # Separate question and answer from origin dictionary
  answer = question["answer"]
  question = question["question"]
  return question, answer


def view_question_list():
  print("Questions:")
  for i in range(1, len(questions) + 1, 1):
    print(questions[f"question_{i}"]["question"])

def add_question(question: str, answer: str, calculateAnswer: bool=False):
  newIndex = len(questions) + 1
  question_name = newIndex + 1
  if calculateAnswer == False:
    questions[f"question_{question_name}"] = {"question": question, "answer": answer}
  else:
    questions[f"question_{question_name}"] = {"question": question, "answer": eval(answer)}