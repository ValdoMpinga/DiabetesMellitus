from django.contrib import admin
from .views import contributionData, diagnosticData, userData
from .models import ChartsModel
import pandas as pd

@admin.register(ChartsModel)
class ChartsModelAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        diagnostic_data = diagnosticData()

        usersData = userData()
        print(usersData)
        parsedMonths = usersData['months']
        parsedUserAmount = usersData['amount']

        contribution_data = contributionData()

        extra_context = {
            'diabetic_predicted': diagnostic_data['diabetic_predicted'],
            'non_diabetic_predicted': diagnostic_data['non_diabetic_predicted'],

            'months': parsedMonths,
            'userMounthAmount': parsedUserAmount,

            "diabetics": contribution_data['diabetics'],
            "non_diabetics": contribution_data['non_diabetics'],
        }

        return super().changelist_view(request, extra_context=extra_context)

    def has_add_permission(self, request, obj=None):
            return False

    def has_change_permission(self, request, obj=None):
            return False

