from django.shortcuts import render
from diagnostic.models import Diagnostic
from register.models import UserModel
from project_support.models import DiabetesSamples
import pandas as pd
import calendar


def charts(request):
    diagnostic_data = diagnosticData()

    usersData = userData()
    parsedMonths = usersData['months']
    parsedUserAmount = usersData['amount']

    contribution_data = contributionData()

    context = {
        'diabetic_predicted': diagnostic_data['diabetic_predicted'],
        'non_diabetic_predicted': diagnostic_data['non_diabetic_predicted'],

        'months': parsedMonths,
        'userMounthAmount': parsedUserAmount,

        "diabetics": contribution_data['diabetics'],
        "non_diabetics": contribution_data['non_diabetics'],
    }
    return render(request, 'charts/charts.html', context)


def diagnosticData():
    diagnostics = Diagnostic.objects.values('diagnosticResult')
    diagnosticFrame = pd.DataFrame(diagnostics)
    diabetic_predicted = (diagnosticFrame['diagnosticResult'] == 1).sum()
    non_diabetic_predicted = (diagnosticFrame['diagnosticResult'] == 0).sum()
    output = {
        'diabetic_predicted': diabetic_predicted,
        'non_diabetic_predicted': non_diabetic_predicted
    }

    return output


def contributionData():
    contributions = DiabetesSamples.objects.values('areYouDiabetic')
    contributionFrame = pd.DataFrame(contributions)
    contributionList = contributionFrame.areYouDiabetic.tolist()
    diabetics = (contributionFrame['areYouDiabetic'] == 1).sum()
    non_diabetics = (contributionFrame['areYouDiabetic'] == 0).sum()

    output = {
        'diabetics': diabetics,
        'non_diabetics': non_diabetics
    }

    return output


def userData():
    pd.set_option('display.max_columns', None)
    users = UserModel.objects.all().values()
    usersFrame = pd.DataFrame(users)
    usersList = usersFrame.date_joined.tolist()

    usersFrame['date_joined'] = pd.to_datetime(usersFrame['date_joined'])
    usersFrame['date_joined'].apply(lambda x: x.date())
    # print(type(usersFrame['date_joined']))
    usersFrame['date_joined'] = usersFrame['date_joined'].dt.month
    print("-------------------")
    usersFrame['date_joined'] = usersFrame['date_joined'].apply(
        lambda x: calendar.month_abbr[x])
    data = usersFrame['date_joined'].value_counts().to_dict()
    print(data)
    months = list(data.keys())
    print("Here: ", type(months))
    amount = list(data.values())
    print(amount)
    output = {
        "months": months,
        "amount": amount
    }
    return output

    # countTry= usersFrame.groupby([usersFrame['date_joined'].dt.month.rename('month')]).agg({'count'})
    # print(countTry)

    # print(a.apply(lambda x: calendar.month_abbr[x]))
    # print("------------------------------------------------")
    # print(usersFrame)
    # usersFrame['month'] =  usersFrame['date_joined'].month
    # print( usersFrame['month'] )
