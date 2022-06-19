from datetime import date
import datetime
today = date.today()


def daysCalculator(userLastContributionDate):
    if userLastContributionDate != None:
        currentDate = datetime.datetime.strptime(
            str(today), '%Y-%m-%d').strftime('%d/%m/%Y')
        currentDate = datetime.datetime.strptime(currentDate, "%d/%m/%Y")
        lastContribuitionDate = datetime.datetime.strptime(
            userLastContributionDate, "%d/%m/%Y")

        daysOfDifference = (currentDate - lastContribuitionDate).days
        if daysOfDifference > 366:
            return  daysOfDifference - 366 
        else:
            return  366 - daysOfDifference
    else:
        return 0
