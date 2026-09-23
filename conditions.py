# 3 conditionals in python


# 1. if condition
# 2. if else condition
# 3. if elif else

# isPass = False

# if isPass:
#     print("The student has passed the exam.")
# else: 
#     print("The student has not passed the exam.")


marks = float(input("Enter the marks of the student: "))
print("The student has got ",marks)

if marks > 90:
    print("The student has got 90% marks")
elif marks > 80: 
    print("The student has got 80% marks")
elif marks > 70: 
    print("The student has got 70% marks")
else: 
    print("The student has failed the exam")


