from django.contrib import admin

# admin
urlpatterns = [
    { 'suffix':'admin', 'view': admin.site.urls },
]
