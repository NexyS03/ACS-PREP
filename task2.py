
while True:
    try:
        r_width = float(input("Enter the width of the room: "))
        break
    except:
        print("enter a number")
while True:
    try:
        r_length = float(input("Enter the length of the room: "))
        break
    except:
        print("enter a number")
while True:
    try:
        un_width = float(input("Enter the width of unpaintable areas: "))
        break
    except:
        print("enter a number")
while True:
    try:
        un_length = float(input("Enter the length of unpaintable areas: "))
        break
    except:
        print("enter a number")
while True:
    try:
        num_coats = float(input("Enter the number of coats of paint requires: "))
        break
    except:
        print("enter a number")
total_paint = ((r_length * r_width - un_length * un_width) * num_coats) / 11
print("The total amount of paint required to paint the room is: ", total_paint, "liters.")

## ACS - A good firts effort
## ACS - Your code needs comments
## ACS - Don't use break .. loops should neveer be infinite and crashed out of!
