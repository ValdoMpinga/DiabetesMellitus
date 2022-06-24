from datetime import date
import datetime
today = date.today()

#Calculates how many days are left for the user to be able to contribute again
def daysCalculator(userLastContributionDate):
    if userLastContributionDate != None:
        currentDate = datetime.datetime.strptime(
            str(today), '%Y-%m-%d').strftime('%d/%m/%Y')
        currentDate = datetime.datetime.strptime(currentDate, "%d/%m/%Y")
        lastContribuitionDate = datetime.datetime.strptime(
            userLastContributionDate, "%d/%m/%Y")

        daysOfDifference = (currentDate - lastContribuitionDate).days
       
        return daysOfDifference
    else:
        return 0
