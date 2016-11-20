import sys
Days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
Months = [["Feb"],["Jan","Mar","May","Jul","Aug","Oct","Dec"],["Apr","Sep","Jun","Nov"]] 

testDate = "Thu Nov 10 19:20:52 2016"

dateArray = testDate.split()

isValid = True

if not dateArray[0] in Days:
    print "Day {} is invalid".format(dateArray[0])
    sys.exit()


if not dateArray[1] in Months.flatten():
    print "Month {} is invalid".format(dateArray[1])
    sys.exit()
    

if dateArray[1] in Months[0] and dateArray[2] > 28:
    print "Date {} is invalid".format(dateArray[1])
    sys.exit()
elif dateArray[1] in Months[1] and dateArray[2] > 31:
    print "Date {} is invalid".format(dateArray[1])
    sys.exit()
elif dateArray[1] in Months[2] and dateArray[2] > 30:
    print "Date {} is invalid".format(dateArray[1])
    sys.exit()

timeArray = dateArray[3].split(":")

if timeArray[0] > 23:
    print "Time {} is invalid".format(dateArray[3])
    sys.exit()
elif timeArray[1] > 59:
    print "Time {} is invalid".format(dateArray[3])
    sys.exit()
elif timeArray[2] > 59:
    print "Time {} is invalid".format(dateArray[3])
    sys.exit()

if dateArray[4] > 2016:
    print "Year {} is invalid".format(dateArray[4])
    sys.exit()

print "date {} is correct".format(dateArray)
