from django.shortcuts import render

def index(request):
    return render(request, 'testcase/index.html')

def page_with_menu(request, menu_title, pk):
    return render(request, 'testcase/page_with_menu.html', {'menu': menu_title, 'pk': pk})
