questions = {
  "question_1": {
    "question": "What is 1 + 1",
    "answer": ["2", "two"]
  },
  "question_2": {
    "question": "What is 5 x 5",
    "answer": "25"
  }
}


def retrieve_question_and_answer(question_number: int):
  question = questions[f"question_{question_number}"]

  answer = question["answer"]
  question = question["question"]
  return question, answer


def view_question_list():
  print("Questions:")
  for i in range(1, len(questions) + 1, 1):
    print(questions[f"question_{i}"]["question"])
