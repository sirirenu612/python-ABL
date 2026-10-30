
# University Admission Decision Engine

eligible = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print("\nApplicant", i + 1)

    name = input("Enter name: ")
    course = input("Enter course (CSE/ECE/MECH): ").upper()

    maths = float(input("Enter Maths marks: "))
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))

    # Calculate aggregate
    aggregate = (maths + physics + chemistry) / 3

    # Course-specific threshold
    if course == "CSE":
        threshold = 80
    elif course == "ECE":
        threshold = 70
    elif course == "MECH":
        threshold = 60
    else:
        threshold = 101

    # Check eligibility
    if (maths >= 50 and physics >= 50
            and chemistry >= 50
            and aggregate >= threshold):

        print("Eligible for Admission")

        eligible.append([
            name, course, maths, physics,
            chemistry, aggregate
        ])

    else:
        print("Not Eligible for Admission")

# Ranking using bubble sort
for i in range(len(eligible)):
    for j in range(len(eligible) - 1 - i):

        a = eligible[j]
        b = eligible[j + 1]

        if (a[5] < b[5] or
            (a[5] == b[5] and a[2] < b[2]) or
            (a[5] == b[5] and a[2] == b[2]
             and a[3] < b[3])):

            eligible[j], eligible[j + 1] = b, a

# Display ranked list
print("\n===== ADMISSION RANK LIST =====")

if len(eligible) == 0:
    print("No eligible applicants found.")

else:
    for i in range(len(eligible)):
        print("\nRank:", i + 1)
        print("Name:", eligible[i][0])
        print("Course:", eligible[i][1])
        print("Aggregate:", eligible[i][5])

print("\nAdmission Process Completed!")
