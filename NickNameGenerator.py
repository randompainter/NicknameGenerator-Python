# Nickname Generator 
import random

# Global Variables
loop = True

nick_names = ("Crusher", "Buster", "Buzz", "Bolter", "Mathematical Genius", "Coder", "Clown Star", "Apex Predator")

default_name = ("John Doe")

while loop:

  # Print Student Grades Menu
  print("\nMain Menu: " + "(" + default_name +")")

  print("1: Change Name")
  
  print("2: Generate Random Nickname")
  print("3: Display All Nickname")
  print("4: Add Nickname")
  print("5: Remove Nickname")
  print("\n6: EXIT")

  selection = input("\nEnter Selection (1-6): ")

  if selection == "1":
     first_name = str(input("\nPlease enter your first name: "))
     last_name = str(input("Please enter your last name: "))
     default_name = first_name + " " + last_name
     print("\nCurrent name is: " + first_name +  " " + last_name)

  elif selection == "2":
        print("\nRANDOM NICKNAME")
        print("\n" + default_name + " The " + random.choice(nick_names))

  elif selection == "3":
    print("Display All Nickname")
    print("\nALL NICKNAMES")        
    for i in nick_names:
     print("\n" + default_name + " " + "The" + " " + i + " ")
        
  elif selection == "4":
    print("Add Nickname")
    new_nick_name = str(input("\nPlease Enter A New Nickname: "))
  
  elif selection == "5":
    print("Remove Nickname")
  elif selection == "6":
    print("Closing Nickname Generator.......")
    loop = False
  else:
    loop = True


