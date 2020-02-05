from django.http import HttpResponse
def validationprofile(request):
    details=request.POST.get('fname','default')
    print(details)
    return HttpResponse('You are Login')