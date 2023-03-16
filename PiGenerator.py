from PiAlgs import *
import pickle

#Choice of series
while True:
    user = input("[1]Leibniz Series\n[2]Nilakantha Series\n>")
    if user == '1':
        series = 'lei'
        break
    elif user == '2':
        series = 'nil'
        break
    else:
        print("Invalid input")

#Choice of iterations
while True:
    user = input("How many iterations would you like to complete?\n>")
    try:
        int(user)
    except:
        print("Invalid input")
    else:
        iterations = int(user)
        break

#Choice of Data Source
while True:
    user = input("[1]Start fresh\n[2]Use existing PI data\n>")
    if user == '1':
        existingData = False
        break
    elif user == '2':
        existingData = True
        break
    else:
        print("Invalid input")

#Fetches existing data and Validates file (needs more work)
while existingData:
    file = input("Enter the file location for your PI data\n>")
    try:
        readData(file)
    except FileNotFoundError:
        print("Unable to locate file.")
    except:
        print("Error unknown")
    else:
        piDict = readData(file)
        break

#Runs and displays calculations
if existingData == False:
    if series == 'lei':
        data = Pi(iterations).LeibnizSeries
    elif series == 'nil':
        data = Pi(iterations).NilakanthaSeries
else:
    if series == 'lei':
        data = Pi(iterations, piDict).LeibnizSeries
    elif series == 'nil':
        data = Pi(iterations, piDict).NilakanthaSeries  
print("Calculations complete")
print(data)

#Deals with saving data to files
if existingData == True:
    while True:
        user = input("[1]Overwrite same file\n[2]Overwrite different file\n>")
        if user == '1':
            break
        elif user == '2':
            file = input("Enter file location you wish to overwrite, if the file does not exist one will be created.\n>")
            break
        else:
            print("Invalid input")
else:
    file = input("Enter file location you wish to overwrite, if the file does not exist one will be created.\n>")
writeData(file, data)
print("New data saved.")

input()



