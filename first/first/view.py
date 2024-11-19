from django.http import HttpResponse

def first_page(request):
    return HttpResponse("<h1>First Django project</h1>")