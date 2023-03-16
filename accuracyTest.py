from PiAlgs import *

file = open('milPi.txt')

piDict = NilakanthaSeries("new", 1000000)

myPi = str(piDict["calculatedPi"])

realPi = file.read()
t=-1

print(myPi)

while True:
    t = t + 1

    mine = myPi[t]


for i in myPi:
    t = t + 1
    mine = i
    real = realPi[t]
    
