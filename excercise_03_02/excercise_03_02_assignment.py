score = input("Enter Score: ")
# gives the command to try the if statement for letter_grade
try:
    letter_grade = float(score)

# if the try command above does not work, it will print the below
except:
    print("Error with your score input")

# Possible inputs
if  letter_grade >= float(0.9):
    print('A')
elif letter_grade >= float(0.8):
    print('B')
elif letter_grade >= float(0.7):
    print('C')
elif letter_grade >= float(0.6):
	print('D')
elif letter_grade > float(0.6):
    print('F')
