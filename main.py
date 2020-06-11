print('Hello, welcome to trivia')

ans = input('Are you ready to play? (Yes/No) ')
score = 0
totalq = 4 

if ans.lower() == "yes":
    ans = input("1. What is the best programming language? ")
    if ans.lower() == "python":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    ans = input("2. What is 2 + 8 + 9 - 1? ")
    if ans == "18":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    ans = input("3. What is better a 1050ti or 1060 (Graphics Card)? ")
    if ans.lower() == "1060":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    ans = input("4. Who came second in the Stanely Cup finals? ")
    if ans == "knights" or ans.lower() == "vegas":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    print("Thank you for playing, you got", score, "questions correct!")
    mark = (score/totalq) * 100
    print("Mark:", str(mark) + "%")
print("Goodbye")