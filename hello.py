# Student Score Calculator
# Beginner Python Project

print("=== Student Score Calculator ===")

name = input("Enter your name: ")

math = int(input("Enter your Maths score: "))
science = int(input("Enter your Science score: "))
english = int(input("Enter your English score: "))

total = math + science + english
percentage = total / 3

print()
print("=== Result ===")
print("Student:", name)
print("Total Score:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: F")