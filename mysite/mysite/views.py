# I HAVE CREATED THIS FILE
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # about={'name': 'simar' , 'place': 'milky bae'}
    return render(request,'index.html')
    # return HttpResponse("hello Ajooni <a href='/'> <button> press here  </button>  </a>")
def analyze(request):
    # get the text
    djtext= request.POST.get('text', 'default')
    # get the chekbox value for checking
    removepun= request.POST.get('removepunc', 'off')
    caps=request.POST.get('capitalise', 'off')
    newlineremove=request.POST.get('lineremove', 'off')
    count=request.POST.get('charcount', 'off')

    # analyze the text
    punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if removepun=='on':
      analyzed = ""
      for char in djtext:
          if char not in punctuations:
              analyzed = analyzed + char
      params={'para': 'Newtext' , 'AnalyzedText': analyzed}
      djtext=analyzed
      # return render(request,'removepunc.html',params)

    if caps=='on':
        analyzed=""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params={'para': 'Newtext', 'AnalyzedText': analyzed}
        djtext=analyzed
        # return render(request,'removepunc.html',params)

    if newlineremove=='on':
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed= analyzed+ char
        params={'para': 'new line remover', 'AnalyzedText': analyzed}
        djtext=analyzed
        # return render(request,'removepunc.html',params)


    return render(request, 'removepunc.html', params)
    # else:
    #     return HttpResponse("select a valid option")
# def capfirst(request):
#     return HttpResponse("capital first")
# def newlineremove(request):
#     return HttpResponse("remove new line")
# def spaceremove(request):
#     return HttpResponse("remove space")
# def charcount(request):
#     return HttpResponse("count char")
