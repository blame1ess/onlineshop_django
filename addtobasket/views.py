from django.shortcuts import render

def addtobasketView(request):
    return render(request, 'addtobasket/heading.html')
