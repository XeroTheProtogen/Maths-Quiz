def force_float(msg):
  """Checks if the player has inputted a number, and if not,
     catches the ValueError given & instead asks for a valid number"""
  valid = False
  while not valid:
    try:
      number = float(input(msg))
      valid = True
    except ValueError:
      print("\033[1;37;41mPlease input a valid number")
  else:
    return number
    
  