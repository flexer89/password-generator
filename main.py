#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Menu design
while True:
  print("Welcome to the Password Generator!")
  print("----------------------------------")
  print("  1 - Entirely random generator")
  print("  2 - Specified letters, symbols \n      and numbers amount")
  print("----------------------------------")

  choice = int(input("\n\nChoose an option: "))
  password =""

  if choice == 1:
    print(f"You chose option number {choice}.")
    length = int(input("Password length: "))
    #random pick signs: 1 - letter, 2 - symbol, 3 - number
    for i in range (0,length):
      singOption = random.randint(1,3)
      if singOption == 1:
        password += letters[random.randint(0,len(letters)-1)]
      elif singOption == 2:
        password += symbols[random.randint(0,len(symbols)-1)]
      else:
        password += numbers[random.randint(0,len(numbers)-1)]
    print("Your password: " + password)
    input("Press Enter to continue...")
    print("\033[H\033[J", end="")
  elif choice == 2:
    print(f"You chose option number {choice}.")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    for n in range(0,nr_letters):
      password += letters[random.randint(0,len(letters)-1)]
    for n in range(0, nr_symbols):
      password += symbols[random.randint(0,len(symbols)-1)]
    for n in range(0, nr_numbers):
      password += numbers[random.randint(0,len(numbers)-1)]
    rand = ''.join(random.sample(password,len(password)))
    print("Your password: " + rand)
    input("Press Enter to continue...")
    print("\033[H\033[J", end="")
  else:
    print("You chose a wrong option!")
    input("Press Enter to continue...")
    print("\033[H\033[J", end="")


  



  


  