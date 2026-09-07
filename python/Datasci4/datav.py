import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import pandas as pd

data = {
    "Student_ID": [101,102,103,104,105,106,107,108,109,110,111,112],
    "Name": ["Alex","Brian","Cathy","David","Emma","Frank","Grace","Henry","Ivy","Jason","Kyle","Liam"],
    "Age": [19,20,18,21,19,22,20,18,21,19,20,22],
    "Course": ["IT","IT","Business","IT","Design","Business","IT","Design","Business","IT","Design","Business"],
    "Mark": [78,65,91,54,83,72,88,69,95,61,76,58],
    "Study_Hours": [8,5,12,3,9,7,11,6,14,4,8,5],
    "Attendance": [92,81,97,68,89,84,95,78,99,73,87,76]
}

df = pd.DataFrame(data)
hours = np.sort(df["Study_Hours"])
marks = np.sort(df["Mark"])

fig, ax = plt.subplots()

ax.plot(hours, marks)
ax.legend()

ax.set_title("Study Hours vs Marks")
ax.set_xlabel("Study Hours")
ax.set_ylabel("Mark")

plt.grid()

plt.show()

course_count = df["Course"].value_counts()

fig, ax = plt.subplots()

ax.pie(
    course_count,
    labels=course_count.index,
    autopct="%1.1f%%"
)

ax.set_title("Students by Course")

plt.show()

fig, ax = plt.subplots()

ax.hist(df["Mark"], bins=5)

ax.set_title("Distribution of Marks")
ax.set_xlabel("Mark")
ax.set_ylabel("Number of Students")

plt.show()