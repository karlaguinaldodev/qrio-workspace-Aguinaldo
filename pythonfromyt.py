# birth_year = int(input('Birth year: '))
# age = 2025 - birth_year
# print(f"your age is: {age}")

# weight = float(input("Enter your weight in pounds: "))
# kilograms = weight / 2.205
# print(f"Your weight in kilograms is: {kilograms}")

# name = input("What is your name: ")
# if len(name) > 10:
#   print ("Invalid name it must only be 10 characters")
# else:
#   print (f'Hello {name}')

# price_house = 1000000
# buyergood_credit = False

# if buyergood_credit:
#   downpayment = int(price_house * 0.10)
# else:
#   downpayment = int(price_house * 0.20)

# print(f'Your downpayment will be {downpayment}')

# temperature = int(input("Enter todays temperature: "))

# if temperature > 30:
#   print ("It's a Hot day")
# elif temperature < 10:
#   print ("It's a cold day")
# else:
#   print("It's neither hot nor cold")

# name = input("Enter your name min of 3 characters and max of 50 characters: ")

# if len(name) < 3:
#   print("Invalid number of characters")

# elif len(name) > 50:
#   print("Invalid number of character it exceeds")

# else:
#   print(f"Hi and have a good day {name}!")

# weight = float(input("Weight: "))
# kind_weight = input("(L)bs or (K)g: ")

# if kind_weight.upper() == "L":
#   converted = weight / 2.20462262185
#   print (f"You are {converted} kilograms")

# if kind_weight.upper() == "K":
#   converted = weight *  2.205
#   print (f"You are {converted} pounds")

# secret_number = 5
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     user_input = int(input("Guess the number between 1 to 5:"))
#     guess_count += 1
#     if user_input == secret_number:
#         print ("Correct!")
#         break
# else:
#   print ("Game over")
        

# command = ""
# started = False

# while True:
#   command = input(">")
#   if command.lower() == "start":
#       if started:
#           print("Car is already started!")
#       else:
#           started = True
#           print("Car started... Ready to go!")
#   elif command.lower() == "stop":
#         if not started:
#            print("Car is already stopped")
#         else:
#            started = False
#            print("Car Stopped")
#   elif command.lower() == "help":
#       print("""    
# start - to start the car
# stop - to stop the car
# quit - to exit 
#           """)
#   elif command.lower() == "quit":
#     break
#   else:
#     print ("I dont understand that")
 
# prices = [10, 20, 30]

# total = 0
# for price in prices:
#   total += price
# print(f"total: {total}")

# numbers = [1, 1, 1, 1, 5]

# for number in numbers:
#   output = ''
#   for count in range(number):
#     output += 'x'
#   print(output)


# numbers = []
# numbers_limit = 5

# for i in range(numbers_limit):  # Loop to get 5 numbers
#     num = int(input(f'Enter number {i+1}: '))  # Take input and convert to int
#     numbers.append(num)  # Store in the list

# largest = max(numbers)  # Find the largest number
# print(f'The largest number is: {largest}')


# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# for row in matrix:
#   for item in row:
#     print(item)

# numbers = [1, 2, 3, 4, 5]
# numbers.remove(5)
# print(numbers)

# # numbers = [5, 5, 2, 1, 7, 4]
# uniques = []
# for number in numbers:
#   if number not in uniques:
#     uniques.append(number)
# print(uniques)

#i understand it now
numbers = [5, 5, 5, 5, 5, 2, 1, 7, 4, 4, 4, 4]
uniques = []
for number in numbers:
  if number not in uniques:
    uniques.append(number)
print(uniques)

