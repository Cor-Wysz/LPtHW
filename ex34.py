animals = ['bear', 'python3.6', 'peacock', 'kagaroo', 'whale', 'platypus']

Question_1 = input("What is the animal at 1? ")


while Question_1 != 'python 3.6':
    print("Incorrect. Try again.")
    Question_1 = input("What is the animal at 1? ")
    
if Question_1 == 'python 3.6':
    print("Very good. Next question.")
elif Question_1 != 'python 3.6':
    print("Incorrect. Try again.")
