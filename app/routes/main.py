from django.contrib import admin

urlpatterns = [
    { 'suffix':'admin', 'view': admin.site.urls},
]
