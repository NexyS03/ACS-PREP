while True:
	try:
	    pre_ma = float(input("Input the car mileage the last time the car was filed."))
	    break
	except:
	    print("Enter a number")
while True:
    try:
        now_ma = float(input("Input the car mileage now."))
        break
    except:
        print("Enter a number")
while True:
    try:
        liters = float(input("Input the total number of liters taken to fill the tank."))
        break
    except:
        print("Enter a number.")
gallon = liters * 4.546
miles_gallon = float(now_ma - pre_ma) / gallon
print("The number of miles per gallon is : ",miles_gallon)


### ACS - Logically correct
### ACS - Needs comment sin the code.
