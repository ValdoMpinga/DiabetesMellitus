from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import path


@staff_member_required
def admin_charts_view(request):
    return render(request, 'charts/charts.html')


class CustomAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        app_list += [
            {
                'name': 'charts',
                'app_label': 'charts',
                'models': [
                    {
                        'name': 'charts',
                        'object_name': 'charts',
                        'admin_url': '/admin/charts',
                        'view_only': True,
                    }
                ],
            }
        ]
        return app_list

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('/charts', admin_charts_view, name='admin-charts'),
        ]
        return urls
