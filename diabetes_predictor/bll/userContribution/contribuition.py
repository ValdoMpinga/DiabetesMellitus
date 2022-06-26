from datetime import date
import datetime
today = date.today()

# These function validates if the can contribute for the model or not, by checking that at least 366 days as passed after the
# previous contribution


def contributionIntentValidator(userLastContributionDate):
    if(userLastContributionDate == None):
        return 1
    else:
        #converted the current date to string
        currentDate = datetime.datetime.strptime(
            str(today), '%Y-%m-%d').strftime('%d/%m/%Y')
        currentDate = datetime.datetime.strptime(currentDate, "%d/%m/%Y")
        #converted the last contribution date to string
        lastContribuitionDate = datetime.datetime.strptime(
            userLastContributionDate, "%d/%m/%Y")

        daysOfDifference = (currentDate - lastContribuitionDate).days
        print("days difference: ", daysOfDifference)
        if daysOfDifference >= 366:
            print("Can contribute!")
            return 1
        else:
            print("Too early to contribute!")
            if daysOfDifference > 366:
                daysOfDifference = daysOfDifference - 366
            else:
                daysOfDifference = 365 - daysOfDifference
            return { "code": 0, "days": daysOfDifference }
