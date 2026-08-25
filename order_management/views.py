from django.http import HttpResponse

def home(request):
    return HttpResponse("OMS Project Running Successfully")