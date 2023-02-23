from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def action(request):
    return render(request, 'action.html')
def contact(request):
    return render(request, 'contact.html')
def news(request):
    return render(request, 'news.html')
def doctores(request):
    return render(request, 'doctores.html')




