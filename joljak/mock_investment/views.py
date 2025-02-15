from django.shortcuts import render

def dashboard(request):
    return render(request, 'mock_investment/dashboard.html')