from django.contrib import admin
from .models import AI_TrainerCondition
# Register your models here.

class AI_TrainerConditionAdmin(admin.ModelAdmin):
   def has_add_permission(self, request, obj=None):
        return False

   def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(AI_TrainerCondition,AI_TrainerConditionAdmin)
