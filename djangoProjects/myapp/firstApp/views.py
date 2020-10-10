from django.shortcuts import HttpResponse

# Create your views here.
def News(request):
    return HttpResponse("<p>Hi this is Vasanthan<p>")