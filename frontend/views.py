from django.shortcuts import render

'''
YES! You can template views as well
'''
def index(request):
    return render(request, 'index.html')
