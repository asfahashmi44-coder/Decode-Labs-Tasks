# Project 4: The General Knowledge Quiz (Expanded Edition)
# A 10-question interactive game demonstrating Control Flow and Data States.

print("====================================")
print("     WELCOME TO THE DECODELABS      ")
print("       GENERAL KNOWLEDGE QUIZ       ")
print("====================================\n")

# Initialize the score tracking variable
score = 0

# ----------------------------------------------------
# Question 1
# ----------------------------------------------------
print("Question 1: What is the capital of France?")
ans_1 = input("Your answer: ").strip().lower()

if ans_1 == "paris":
    print("✨ Correct!\n")
    score += 1
else:
    print("❌ Wrong. The correct answer is: Paris\n")

# ----------------------------------------------------
# Question 2
# ----------------------------------------------------
print("Question 2: Which planet is known as the Red Planet?")
print("A) Venus\nB) Mars\nC) Jupiter")
ans_2 = input("Choose your option (A, B, or C): ").strip().upper()

if ans_2 == "B":
    print("✨ Correct!\n")
    score += 1
else:
    print("❌ Wrong. The correct answer is: B) Mars\n")

# ----------------------------------------------------
# Question 3
# ----------------------------------------------------
print("Question 3: How many continents are there on Earth?")
ans_3 = input("Your answer: ").strip()

if ans_3 == "7":
    print("✨ Correct!\n")
    score += 1
else:
    print("❌ Wrong. The correct answer is: 7\n")

# ----------------------------------------------------
# Question 4
# ----------------------------------------------------
print("Question 4: What is the largest ocean on Earth?")
ans_4 = input("Your answer: ").strip().lower()

if ans_4 == "pacific" or ans_4 == "pacific ocean":
    print("✨ Correct!\n")
    score += 1
else:
    print("❌ Wrong. The correct answer is: Pacific Ocean\n")

# ----------------------------------------------------
# Question 5
# ----------------------------------------------------
print("Question 5: Which animal is known as the 'Ship of the Desert'?")
ans_5 = input("Your answer: ").strip().lower()

if ans_5 == "camel":
    print("✨ Correct!\n")
    score += 1
else:
    print("❌ Wrong. The correct answer is: Camel\n")

# ----------------------------------------------------
# Question 6
# ----------------------------------------------------
print("Question 6: How many colors are there in a standard rainbow?")
ans_6 = input("Your answer: ").strip()

if ans_6 == "7":
    print("✨ Correct!\n")
    score += 1
else:
    print("❌ Wrong. The correct answer is: 7\n")

# ----------------------------------------------------
# Question 7
# ----------------------------------------------------
print("Question 7: Which gas do humans need to breathe to survive?")
ans_7 = input("Your answer: ").strip().lower()

if ans_7 == "oxygen":
    print("✨ Correct!\n")
    score += 1
else:
    print("❌ Wrong. The correct answer is: Oxygen\n")

# ----------------------------------------------------
# Question 8
# ----------------------------------------------------
print("Question 8: What is the hardest natural substance on Earth?")
ans_8 = input("Your answer: ").strip().lower()

if ans_8 == "diamond":
    print("✨ Correct!\n")
    score += 1
else:
    print("❌ Wrong. The correct answer is: Diamond\n")

# ----------------------------------------------------
# Question 9
# ----------------------------------------------------
print("Question 9: Which country is home to the Kangaroo?")
ans_9 = input("Your answer: ").strip().lower()

if ans_9 == "australia":
    print("✨ Correct!\n")
    score += 1
else:
    print("❌ Wrong. The correct answer is: Australia\n")

# ----------------------------------------------------
# Question 10
# ----------------------------------------------------
print("Question 10: What is the boiling point of pure water at sea level?")
print("A) 50°C\nB) 100°C\nC) 200°C")
ans_10 = input("Choose your option (A, B, or C): ").strip().upper()

if ans_10 == "B":
    print("✨ Correct!\n")
    score += 1
else:
    print("❌ Wrong. The correct answer is: B) 100°C\n")


# ----------------------------------------------------
# Final Summary Wrap-up
# ----------------------------------------------------
print("====================================")
print("             GAME OVER              ")
print("====================================")
print(f"Your final score is: {score} out of 10!")

if score == 10:
    print("Perfect score! Exceptional mastery of logic and trivia! 🏆")
elif score >= 5:
    print("Great job! You passed the mastery phase comfortably.")
else:
    print("Good try! Run the script again to beat your previous score.")
    