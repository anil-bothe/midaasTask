from django.shortcuts import render

# temp
def home(request):
    return render(request, 'pages/index.html')
