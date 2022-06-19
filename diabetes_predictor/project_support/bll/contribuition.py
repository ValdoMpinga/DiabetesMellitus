from datetime import date
import datetime
today = date.today()


def contributionIntentValidator(userLastContributionDate):
    if(userLastContributionDate == None):
        return 1
    else:
        currentDate = datetime.datetime.strptime(
            str(today), '%Y-%m-%d').strftime('%d/%m/%Y')
        currentDateString = currentDate
        currentDate = datetime.datetime.strptime(currentDate, "%d/%m/%Y")
        lastContribuitionDate = datetime.datetime.strptime(
        userLastContributionDate, "%d/%m/%Y")

        daysOfDifference = (currentDate - lastContribuitionDate).days
        print("diff",daysOfDifference)
        if daysOfDifference >= 366:
            # userModel.UserModel.objects.filter(
            # email=request.user).update(contribuition_date=currentDateString)
            # saveUserContribute(userContribute)
            print("contributed!")
            return 1
        else:
            print("Early to contribute!")
            if daysOfDifference > 366:
                daysOfDifference = daysOfDifference - 366
            else:
                daysOfDifference = 365 - daysOfDifference
                
            return {
                "code": 0,
                "days": daysOfDifference
            }
