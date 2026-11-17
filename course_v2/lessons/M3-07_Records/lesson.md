---
id: "3.7"
title: "Records and Fields"
module: 3
module_title: "Data Structures"
next: "Tuples and Sets"
minutes: 7.26
thumb_code: 'student["name"]'
goals: ["What a record and a field are", "A dictionary as a record", "A list of records, like a table", "Looping through records to make a report"]
youtube:
  title: "Python Lesson 3.7: Records and Fields - Lists of Dictionaries | Introduction to Python"
  description: |
    How do real programs store details about lots of people or things? Ziggy the Python explains records and
    fields with a student card and a table, stores one record as a dictionary, builds a list of records, loops
    through them to print a report, finds the top score, and adds a new field to every record.
    For beginners aged 7 to 20.
  tags: [python records, list of dictionaries python, python data structures, fields and records, learn python, fun skill builders]
---

<!-- Booklet chapter 3: records and fields. -->

## INTRO
Hello, Happy Learners! It's Ziggy the Python here. A game needs to remember lots of details about every player: their name, level, score and more. A school needs details about every student. Today we'll combine dictionaries and lists to store records, which is exactly how real apps and databases organise their information.

## STUDY | Records and fields
@ snippet Name:   Asha\nYear:   7\nScore:  88\nClub:   chess
Think of a library card or a student card. It holds several details about one person: a name, a year group, a score and a club. All the details about one thing, kept together, is called a record.
@ point Record = all the details about ONE thing
A record is the whole card: all the details about one person, one pet, one book or one game character.
@ point Field = one detail inside the record
Each separate detail is called a field. Name is a field. Year is a field. Score is a field. Every record of the same kind has the same fields, but different values.
@ table Name | Year | Score | Club ; Asha | 7 | 88 | chess ; Leo | 8 | 72 | art ; Mia | 7 | 95 | robotics
When we have many records, we can draw them as a table. Each row is one record, and each column is one field. If you've seen a spreadsheet, or a contacts list on a phone, you've seen records and fields.

## STUDY | Records in Python
@ snippet student = {"name": "Asha", "year": 7,\n           "score": 88, "club": "chess"}
In Python, a dictionary makes a perfect record. Each field name is a key, and each detail is a value.
@ point One record = one dictionary
So one record is one dictionary. To get a field, we use its key: student, square bracket, name.
@ point Many records = a list of dictionaries
And many records are stored as a list of dictionaries. The list keeps them in order, and each dictionary holds one record. It's a table, made of the two data structures we already know.
@ point records[1]["name"]: which record, then which field
To get one detail out of the table, use two steps: first the index of the record in the list, then the key of the field. Records one, name, means: the second record's name.

## CODE | student.py
```python
student = {"name": "Asha", "year": 7,
           "score": 88, "club": "chess"}
print(student["name"])
print(f"{student['name']} is in year {student['year']}.")
student["score"] = student["score"] + 5
student["age"] = 12
print(student)
```
@ line 1-2 | One record: four fields
Lines one and two make one record, a dictionary with four fields: name, year, score and club.
@ line 3 | Read one field
Line three reads the name field.
@ line 4 | Fields inside an f-string: use single quotes inside
Line four uses two fields inside an F string. Look closely: the F string uses double quotes, so inside the curly brackets, the keys use single quotes. Using double quotes inside would end the string too early.
@ line 5 | Update a field
Line five updates the score field, adding five bonus points.
@ line 6 | Add a brand new field
And line six adds a brand new field: age.
@ line 7
Line seven prints the whole record.
@ predict 6 | What will the score be? Where will age appear?
What will the score be now, and where in the record will age appear?
@ run | 93 points, and a new age field at the end
Run. Asha. Asha is in year seven. And the record now has a score of ninety three, and a new age field at the end.

## CODE | class_list.py
```python
students = [
    {"name": "Asha", "year": 7, "score": 88},
    {"name": "Leo", "year": 8, "score": 72},
    {"name": "Mia", "year": 7, "score": 95},
]
print(len(students), "records")
print(students[1]["name"])
for s in students:
    print(f"{s['name']:<6} year {s['year']}  {s['score']}")
```
@ say
Now a whole table of records: a list of dictionaries.
@ line 1 | The list opens
Line one opens a list.
@ line 2-4 | One dictionary per line = one record per row
Lines two to four each hold one record. Writing one record per line makes it look like a table. The comma after the last record is allowed, and it makes adding another one easier.
@ line 5 | The list closes
Line five closes the list.
@ line 6 | How many records?
Line six counts the records.
@ line 7 | Record 1, field "name"
Line seven gets record one's name. Which student is that?
@ predict 4 | Who is students[1]?
Remember that indexes start at zero.
@ run | 3 records; students[1] is Leo
Run. Three records. And record one is Leo, the second student.
@ line 8 | Loop: s is one whole record each time
Line eight loops through the list. Each time round, s is one whole record, one dictionary.
@ line 9 | Print a report line; :<6 pads the name to 6 characters
Line nine prints a report line. The colon, less than sign and six after the name is a formatting trick: it pads the name to six characters wide, so the columns line up.
@ run | A neat report, one line per record
Run. A neat report, with the names, years and scores in tidy columns. Any number of students, and the same two lines of loop would print them all.

## CODE | top_student.py
```python
students = [
    {"name": "Asha", "score": 88},
    {"name": "Leo", "score": 72},
    {"name": "Mia", "score": 95},
]
best = students[0]
total = 0
for s in students:
    total = total + s["score"]
    if s["score"] > best["score"]:
        best = s
print("Top student:", best["name"], best["score"])
print("Class average:", round(total / len(students), 1))
```
@ say
Let's answer some questions about our data: who has the top score, and what's the average?
@ line 1-5 | Three records
Three records with names and scores.
@ line 6 | Start by assuming the first record is the best
Line six says: to start with, let's assume the first student is the best. We'll check everyone else against them.
@ line 7 | A total for the average
Line seven starts a total for the average.
@ line 8-9 | Add every score to the total
The loop adds each score to the total.
@ line 10-11 | Higher than the best so far? They're the new best
And lines ten and eleven are another sneak peek at if. If this student's score is higher than the best so far, they become the new best. It's like holding the winner's trophy and passing it on whenever someone beats it.
@ line 12-13 | Report the results
Then we print the top student, and the class average.
@ predict 6 | Who wins? What's the average?
Who will be the top student, and what will the average be?
@ run | Mia, 95; average 85.0
Run. Top student: Mia, with ninety five. Class average: eighty five point zero. Eighty eight plus seventy two plus ninety five is two hundred and fifty five, divided by three is eighty five. This keep the best so far pattern is how computers find the highest score, the cheapest price, or the fastest lap.

## STUDY | Common mistakes
@ table Mistake | What happens ; f"{s["name"]}" | SyntaxError in older Pythons: use 'name' inside ; s[name] (no quotes) | NameError: the key is a string ; students["name"] | TypeError: pick a record first ; records with different keys | KeyError when a field is missing
Common mistakes with records. Using double quotes for a key inside a double quoted F string can cause errors, so use single quotes inside. Forgetting the quotes around a field name makes Python look for a variable. Asking the list for a field before choosing a record gives a TypeError. And if one record is missing a field, looking it up gives a KeyError, so keep every record's fields the same.

## REVISE | Quick revise
@ point A record holds all the details of one thing; a field is one detail
A record holds all the details about one thing. A field is one detail.
@ point One record = one dictionary; keys are the field names
In Python, one record is a dictionary, and the keys are the field names.
@ point A table = a list of dictionaries
A table of records is a list of dictionaries.
@ point records[i]["field"]; loop with for r in records
Use the index then the key for one detail, and a loop to go through every record.

## PRACTICE | Add a field
@ task pets = [{"name": "Biscuit", "type": "dog"},\n        {"name": "Luna", "type": "cat"}]\n1. Add an "age" field to each pet\n2. Loop and print: Biscuit the dog is 4
Your turn. Start with two pet records, each with a name and a type. Add an age field to each pet. Then loop through the records and print a sentence for each, like: Biscuit the dog is four.
@ hint pets[0]["age"] = 4, then an f-string with three fields
Hint: set pets zero age, and pets one age. Then use an F string with three fields, using single quotes for the keys.
@ pause 15
Pause the video and try it.

## ANSWER | pets_report.py
```python
pets = [{"name": "Biscuit", "type": "dog"},
        {"name": "Luna", "type": "cat"}]
pets[0]["age"] = 4
pets[1]["age"] = 2
for p in pets:
    print(f"{p['name']} the {p['type']} is {p['age']}")
```
@ line 1-2
Two pet records.
@ line 3-4
Add an age field to each one: first choose the record, then the field.
@ line 5-6
Then loop, and print a sentence with three fields.
@ run
Run. Biscuit the dog is four. Luna the cat is two. You've just built a tiny database!

## OUTRO
Excellent! Lists of dictionaries are how real apps store their data, and now you can use them too. Next time, we'll meet two more data structures: tuples, which can't change, and sets, which never have duplicates. Like, share and subscribe, and keep coding. Happy Learning!
