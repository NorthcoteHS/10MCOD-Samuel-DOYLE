bye = 'y'
while bye=='y':
    #Welcome and disclaimer
    print("Hello and welcome to the amazing #Retirement financial advisor")
    print("Note: this program is not an certified financial advisor")
    print("Second note: please do not include the % sign or commas when answering a question")
    print(" ")

    #get info about user superannuation
    print("Part One- Superannuation")
    print("Please answer all questions in numerical form only")
    paIncome=int(float(input("What is your combined annual household income? ")))
    age=int(float(input("What is your current age? ")))
    superr=int(float(input("What is your current combined household superannuation balance? ")))

    #tell user how much more superannuation they need
    difference=250000-superr
    if difference>0:
        print("You need", difference, "more dollars in superannuation to retire, assuming you have a paid-off house")
        years=65-age
        yearly=difference/years
        superPercen=round(yearly/paIncome*1000)
        superPercent=superPercen/10
        print("You need to put", str(yearly), "dollars into your superannuation account each year to retire,", str(superPercent)+"% of your annual income")
    else:
        print("Congratulations! You have enough superannuation to retire!")

    #5600pm is australian average
    #get info about user spending
    print("Part Two- Spending")
    print("Please answer all questions in numerical form only")
    housing=int(float(input("How much does your household spend on mortgage/rent per month? ")))
    bills=int(float(input("How much does your household spend on utilities per month? ")))
    food=int(float(input("How much does your household spend on groceries per month, excluding restaurants? ")))
    other=int(float(input("How much does your household spend on other items per month?- e.g. clothes, pets, entertainment ")))
    total=housing+bills+food+other
    pmIncome=paIncome/12
    yearSpend=total*12
    #get user spending as a percentage of user income
    spending=yearSpend/paIncome*100
    print("Your spending is", str(spending), "% of your income")
    #compare monthly spending to Australian average
    if spending>5700:
        print("Your spending is more than the average")
    elif spending<5400:
        print("Your spending is less than the average")
    else:
        print("Your spending is average")
    #compare housing cost to Australian average
    if housing>2000:
        print("Your cost of housing is above average")
    elif housing<1600:
        print("Your cost of housing is below average")
    else:
        print("Your cost of housing is average")
    #compare utility cost to Australian average
    if bills>340:
        print("Your cost of utilities is above average")
    elif bills<260:
        print("Your cost of utilities is below average")
    else:
        print("Your cost of utilities is average")
    #compare food cost to Australian average
    if food>640:
        print("Your cost of food is above average")
    elif food<440:
        print("Your cost of food is below average")
    else:
        print("Your cost of food is average")


    #get info about user savings
    print("Part Three- Saving")
    print("Please answer all questions in numerical form only")
    savings=int(float(input("What is your current non-super savings balance? ")))
    save=int(float(input("How much non-super money do you save per month? ")))
    saveROI=int(float(input("What is the interest rate on your savings per year?, e.g. answer '2' for 2%pa ")))
    #calculate how much the user needs for adequate financial security
    three=total*3
    more=three-savings
    moreTime=more/save
    if more>0:
        print("Based on your current spending habits, you need $"+str(three), "in liquid savings to be financially secure in case of an emergency or opportunity")
        print("Therefore, you need", str(more), "more dollars in savings.")
        print("This will take you", str(moreTime), "months at your current savings rate")
    else:
        print("Based on your current spending habits, you need $"+str(three), "In liquid savings to be financially secure in case of an emergency or opportunity. You have $"+str(savings), ". Good job!")
    losingToInflation=1.9-saveROI
    winningInflation=saveROI-1.9
    if saveROI==1.9:
        print("Your savings ROI is equal to inflation. You should save your money somewhere with a higher ROI")
    elif saveROI<1.89:
        print("Your savings ROI is", str(losingToInflation)+"% less than inflation, therefore, you are losing money. You should save your money somewhere with a higher ROI")
    elif saveROI>1.91:
        print("Your savings ROI is", str(winningInflation)+"% more than inflation, therefore you are making money!")



    #get info about user investments
    print("Part Four- Investing")
    yesNo=input("Are you currently making investments other than superannuation? (yes or no) ").lower()
    yesNo=yesNo.strip()
    if yesNo=='yes':
        risk=input("Which of these best matches your investment? \nA. low risk e.g. guaranteed term deposit or bank account \nB. medium risk e.g. managed fund, ETFS, shares, property \nC. high risk e.g. futures, options, venture capital\n")
        returns1=int(float(input("What was your return on investment in 2013? ")))
        returns2=int(float(input("What was your return on investment in 2014? ")))
        returns3=int(float(input("What was your return on investment in 2015? ")))
        returns4=int(float(input("What was your return on investment in 2016? ")))
        returns5=int(float(input("What was your return on investment in 2017? ")))
        avROI=(returns1+returns2+returns3+returns4+returns5)/5
        print("Your average ROI is", avROI, "%pa")
    #average rate of inflation for last 5 years is 1.896%pa
        if avROI<1.9:
              print("You are currently making negative profits on your investment due to inflation.")
        elif avROI>1.9 and avROI<=4:
              print("You are currently making a small profit on your investment.")
        elif avROI>4 and avROI<7:
              print("You are currently making a reasonably good profit on your investment.")
        else:
              print("You are making awesome profits! congratulations!")
        if risk=='A':
              print("You should aim for investments with higher risks and returns")
        elif risk=='C' and years<7:
              print("Assuming you will retire in", years, "years, you might want to aim for investments with lower risks")
        elif risk=='C' and years>7 and avROI>5:
              print("Your investment seems great, just remember to switch to lower risk closer to retirement!")
        elif risk=='C' and years>7 and avROI<5:
              print("You might want to go for an invesment that is less risky and creates higher returns")
        elif risk=='B' and avROI>5:
              print("Your investment has a great risk-to-return ratio! Continue what you're doing!")
        else:
              print("Your investment is a good level of risk, but you should switch to something with higher returns.")
    elif years<7:
        print("Assuming you retire in", years, "years, you should make diversified, medium-to-low risk investments (expected to return negative profits 1 to 2 years out of 20) ")
    elif years>7 and years<20:
        print("Assuming you retire in", years, "years, you should make diversified, medium-to-high risk ivestments (expected to return negative profits 2 to 3 years out of 20) ")
    else:
        print("Assuming you retire in", years, "years, you should make diversified, high risk investments (expected to return negative profits 4 to 5 years out of 20) ")
    print("Thanks for using #Retirement!")
    bye=input("Press x to leave or y to go again! ")
