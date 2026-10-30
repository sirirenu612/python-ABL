import numpy as np

# Input number of students and subjects
n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))

# Input marks matrix
marks = np.zeros((n, m))

for i in range(n):
    for j in range(m):
        marks[i][j] = int(input(f"Enter marks of student {i+1}, subject {j+1}: "))

# Row-wise statistics
print("\nStudent Statistics:")
for i in range(n):
    print("Student", i+1)
    print("Total:", np.sum(marks[i]))
    print("Average:", np.mean(marks[i]))

# Column-wise statistics
print("\nSubject Statistics:")
for j in range(m):
    print("Subject", j+1)
    print("Total:", np.sum(marks[:, j]))
    print("Average:", np.mean(marks[:, j]))

# Top performer
averages = np.mean(marks, axis=1)
top = np.argmax(averages)

print("\nTop Performer: Student", top+1)
print("Highest Average:", averages[top])

# Low-performing subjects
threshold = float(input("\nEnter low average threshold: "))

print("Low Performing Subjects:")
for j in range(m):
    if np.mean(marks[:, j]) < threshold:
        print("Subject", j+1, "Average:", np.mean(marks[:, j]))

print("\nAnalysis Completed")