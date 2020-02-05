from django.shortcuts import render

def index(request):
    return render(request,'formfile.html')

def coding(request):
    data=request.GET.get('text','default')
    punc=request.GET.get('punc','off')
    uppers=request.GET.get('upper','off')
    data1=''
    Punctuation='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    if punc=='on' and uppers=='off':
        for char in data:
            if char not in Punctuation:
                data1=data1+char

    elif uppers=='on' and punc=='off':
        for char in data:
            data1=data1+char.upper()

    elif punc=='on'and uppers=='on':
        for char in data:
            if char is not '\n':
                if char not in Punctuation:
                    data1=data1+char.upper()



    a={'value':data1}
    return render(request,'result.html',a)
