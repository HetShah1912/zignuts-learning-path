# WAP to enter marks of 3 subjects from the user and store them in a dictionary, start with empty dictionary and add one by one, subject name as key, marks as value

marks = {}
marks["maths"] = 90
marks["science"] = 78
marks["english"] = 89
marks["social science"] = 75
marks.update({"general" : 86})
print(marks)