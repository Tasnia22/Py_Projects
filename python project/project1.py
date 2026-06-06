def calculate_grade(avg):
    if avg >= 80:
        return "A+"
    elif avg >= 70:
        return "A"
    elif avg <= 40:
        return "F"
    else:
        return "B"

#student info

name = input("Enter your name: ")
math = float(input("Enter Your math  score: "))
English = float (input("Enter English score: "))
avg =(math+English)/2
calculated_grade = calculate_grade(avg)

print("\n===== RESULT =====")
print("Name:", name)
print("Total Marks:", round(avg * 2, 2))
print("Average:", round(avg, 2))
print("Grade:", calculated_grade)