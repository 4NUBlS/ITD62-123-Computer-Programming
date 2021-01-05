import json

student_info = {
    "name" : "xxxxxx",
    "surname" : "xxxxxx",
    "student_id" : 00000000,
    "age" : 20,
    "gpa" : 4.00
}

student_address = {
    "house_number" : 1,
    "village" : 1,
    "sub_district" : "sub_district",
    "district" : "district",
    "province" : "province",
    "postcode" : 80000
}

student = {
    "student_info" : student_info,
    "student_address" : student_address
}

for x, y in student.items():
    print(x, y)