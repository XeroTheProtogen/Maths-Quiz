from time import sleep
import questions as quest


def quiz():
  """The main function of the program & the sum of the functions within it"""
  # Play the intro
  intro()
  score = questions()
  print(f"Score is {score}, and the minimum score is 6/10")

def quiz_calibration():
  """Introductory questions used to calibrate possible questions in the quiz"""
  #Initialize boolean variables
  sub = False
  mul = False
  div = False

  #Ask the player how comfortable they are with certain types of questions
  #Assess the answers to determine which boolean variables are made true or false
  #(Too messy to try and explain, unfortunately)
  loop = True
  #This loop is used to check what math operations the user is fine to work with
  while loop == True:
    subtraction = input("Are you fine with subtraction and negative numbers? Y/N").strip().lower()
    if subtraction in ("yes", "y"):
      sub = True
      multiplication = input("Are you fine with multiplication? Y/N").strip().lower()
      if multiplication in ("yes, y"):
        mul = True
        division = input("Are you fine with division and decimals? Y/N \n(Calculator recommended)").strip().lower()
        if division in ("yes", "y"):
          div = True
          loop = False
          break
        elif division not in ("no", "n"):
          print("Please repeat that")
        else:
          loop = False
          break
      elif multiplication not in ("no", "n"):
        print("Please repeat that")
      else:
        loop = False
        break
    elif subtraction not in ("no", "n"):
      print("Please repeat that")
    else:
      loop = False
      break
  return sub, mul, div

def intro():
  print("""====================
  Welcome to the 2023 Math Quiz
  =========================""")
  sleep(3)
  print("""====================
  You'll be answering ten questions, and if you get 2 thirds of them correct,
  you win!
  =========================""")
  sleep(5)
  print("""====================
  But first, we need to get an idea of your maths competence, 
  so we'll ask you a few introductory questions
  =========================""")
  sleep(6)
  sub, mul, div = quiz_calibration()
  questions(sub, mul, div)

def questions(subtraction:bool, multiplication:bool, division:bool):
  """Main quiz function, which both generates and asks the player questions, alongside
  retrieving the player's score for assessment."""
  questionsAndAnswers = quest.generate_questions(subtraction, multiplication, division)
  score = quest.ask_consequtive_questions(questionsAndAnswers)
  return score