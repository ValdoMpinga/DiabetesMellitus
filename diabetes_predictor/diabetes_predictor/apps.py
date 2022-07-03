from django.contrib.admin.apps import AdminConfig


class CustomAdminConfig(AdminConfig):
    default_site = 'diabetes_predictor.admin.CustomAdminSite'
