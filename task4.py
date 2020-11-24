import math
while True:
    try:
        students = int(input("The number of students."))
        break
    except:
        print("Enter an integer")
while True:
    try:
        books = int(input("The number of books."))
        break
    except:
        print("Enter an integer")
books_per_student = int(math.floor(books / students))
print("The number of book(s) per student is ", books_per_student)
books_left = books - books_per_student*students
print("The number of book(s) left over is ", books_left)


name = input("Enter a name: ")
print("The length of the name is: " + str(len(name)))

## ACS - Code doens't work
## Needs comments
