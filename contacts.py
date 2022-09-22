contacts = {
    "number":4,
    "students": [
        {"name":"Lisa1", "email":"123@abc.com"},
        {"name":"Lisa2", "email":"1234@abc.com"},
        {"name":"Lisa3", "email":"1235@abc.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"]) 