def credit_rating(score):
    if(score >= 300 and score <= 579):
        return 'Poor'
    elif(score >= 580 and score <= 669):
        return 'Fair'
    elif(score >= 670 and score <= 739):
        return 'Good'
    elif(score >= 740 and score <= 799):
        return 'Very Good'
    elif(score >= 800 and score <= 850):
        return 'Exceptional'
    else:
        return 'Invalid Score'

continueLoop = True
while continueLoop != False:
    score = int(input("Please enter a score: "))
    result = credit_rating(score)
    print(result)

    cont = int(input("Please enter 0 to stop entering scores: "))

    if(cont == 0):
        continueLoop = False
