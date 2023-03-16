def LeibnizSeries(piDict, iterations):
#Leibniz formula for π
#π=(4/1)-(4/3)+(4/5)-(4/7)+(4/9)-(4/11)+(4/13)-(4/15)...
#https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    import decimal
    from tqdm import tqdm
    #decimal.getcontext().prec = 10000


    if piDict == 'new':
        #Assigns starting variables
        t = decimal.Decimal(0)
        pi = decimal.Decimal(4)    
    else:
        #Unpackages dictionary
        pi = piDict["calculatedPi"]
        t = piDict["totalIterations"]

    #Sets variables based on number of iterations completed
    d = t * 2 + 1
    if d % 2 == 0:
        mathSym = 'sub'
    else:
        mathSym = 'add'

    #Performs the calculations
    for i in range(iterations):
        t = t + 1
        if mathSym == 'sub':
            pi = pi - (4 / d)
            mathSym = 'add'
        else:
            pi = pi + (4 / d)
            mathSym = 'sub'
        d = d + 2
        print("         " + str(t))
        print(len(str(pi)))

    #Packages and returns dictionary
    piDict = {
        "calculatedPi" : pi,
        "totalIterations" : t,
    }

    return(piDict)

def NilakanthaSeries(piDict, iterations):
#Nilakantha series for π
#π=3+4/(2·3·4)-4/(4·5·6)+4/(6·7·8)-4/(8·9·10)+4/(10·11·12)-4/(12·13·14)...
#https://www.mathscareers.org.uk/calculating-pi/

    import decimal
    decimal.getcontext().prec = 10000

    if piDict == 'new':
        #Assigns starting variables
        t = 0
        pi = decimal.Decimal(3)
        
    else:
        #Unpackages dictionary
        pi = piDict["calculatedPi"]
        t = piDict["totalIterations"]
        
        
    d = [t*2+2 , t*2+3, t*2+3]
    if d % 2 == 0:
        mathSym = 'add'
    else:
        mathSym = 'sub'

    #Performs the calculations
    for i in range(iterations):
        t = t + 1
        if mathSym == 'add':
            pi = pi + 4 / (d[0] * d[1] * d[2])
            mathSym = 'sub'
        else:
            pi = pi - 4 / (d[0] * d[1] * d[2])
            mathSym = 'add'
        d = [d[2], d[2]+1, d[2]+2]
        print("         " + str(t))
        print(len(str(pi)))

    #Packages and returns dictionary
    piDict = {
        "calculatedPi" : pi,
        "totalIterations" : t,
    }

    return(piDict)


LeibnizSeries('new', 100)