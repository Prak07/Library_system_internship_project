from django.http import HttpResponse,JsonResponse

def home(request):
    return JsonResponse({"hello":"hi"})