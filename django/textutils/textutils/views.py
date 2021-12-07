# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    #check with checkbox is on 
    if removepunc=="on":
        punctuations = '''!()-{,}[];:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed puncuations', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
        
    elif(fullcaps=="on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper', 'analyzed_text': analyzed}
    # analyze the text
        return render(request, 'analyze.html', params)
        
    elif(extraspaceremover=='on'):
        analyzed =""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
    # analyze the text
        return render(request, 'analyze.html', params)
    
    elif(newlineremover=='on'):
        analyzed =""
        for char in djtext:
            if char!='\n':
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    # analyze the text
        return render(request, 'analyze.html', params)
    
    elif(charcount=='on'):
        count=0
        for i in djtext:
            count+=1
        params = {'purpose': 'Number of CHaracters', 'analyzed_text': count}
    # analyze the text
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Please tick the box!")

 # def capfirst(request):
#    return HttpResponse("This is a Capitalize first")
# def newlineremove(request):
#    return HttpResponse("This is a New line remove")
# def spaceremove(request):
#    return HttpResponse("This is a Space remove")
# def charcount(request):
#   return HttpResponse("This is a Char count")
