from django.shortcuts import render
def html(request):
    a={'name':'Pradip','location':'KTM'}
    return render(request,'formfile.html',a)
