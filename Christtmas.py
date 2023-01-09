# Creating Functions and calling them
def profit(x, y):
    result = x * y
    return result


Amazon = profit(2000, 10)
print(Amazon)

Microsoft = profit(3000, 20)
print(Microsoft)

# String Methods: capitalize() and strip()
legend = "   my name  is   a legend    "
karma = legend.strip().title()
print(karma)

# String Method 2: splitting text into two using split()
career = "Data Analyst"
application, role = career.split(" ")
print(application, role, end="\n")

Apple = profit(5000, 0.6)
print(Apple)

apples = [1, 4, 6, 9, 10]
for i in apples:
    print(i)

# Conditionals: Assign grades to KCSE Students
score = int(input("Score: "))

if score >= 80 and score <= 90:
    print("Grade: A")
elif score >= 70 and score < 80:
    print("Grade: B")
elif score >= 60 and score < 70:
    print("Grade: C")
elif score >= 50 and score < 60:
    print("Grade: D")
else:
    print("Grade: E")
