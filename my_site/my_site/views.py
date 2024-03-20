from django.http.response import HttpResponse

def home_view(req):
    return HttpResponse("Home page")