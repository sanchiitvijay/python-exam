subjects = [
    "Data Structures",
    "Database Management Systems",
    "Operating Systems",
    "Computer Networks",
    "Software Engineering",
    "Python Programming Lab",
    "Web Technologies",
    "Discrete Mathematics"
]

print("Subject list:")
for subject in subjects:
    print(subject)

print("\n2nd element:", subjects[1])
print("5th element:", subjects[4])

print("\nFirst 4 elements:", subjects[:4])

print("\nLast 4 elements:", subjects[-4:])

if "Python Programming Lab" in subjects:
    print("\n'Python Programming Lab' is available in the list.")
else:
    print("\n'Python Programming Lab' is not available in the list.")

subjects.append("Machine Learning")
print("\nList after appending 'Machine Learning':", subjects)

subjects.insert(3, "Artificial Intelligence")
print("\nList after inserting 'Artificial Intelligence' at index 3:", subjects)

subjects.remove("Software Engineering")
print("\nList after removing 'Software Engineering':", subjects)

popped_subject = subjects.pop()
print("\nList after popping the last element:", subjects)
print("Popped element:", popped_subject)
