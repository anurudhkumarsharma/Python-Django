# I have created this file
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')

def feature(request):
    return render(request, 'feature.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # check with checkbox is on
    if removepunc == "on":
        punctuations = '''!()-{,}[];:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed puncuations', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper', 'analyzed_text': analyzed}
    # analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
    # analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    # analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(charcount == 'on'):
        count = 0
        for i in djtext:
            count += 1
        params = {'purpose': 'Number of CHaracters', 'analyzed_text': count}
    if(removepunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on" and charcount != "on"):
        return HttpResponse("Please select atleast one box!")

    return render(request, 'analyze.html', params)

 # def capfirst(request):
#    return HttpResponse("This is a Capitalize first")
# def newlineremove(request):
#    return HttpResponse("This is a New line remove")
# def spaceremove(request):
#    return HttpResponse("This is a Space remove")
# def charcount(request):
#   return HttpResponse("This is a Char count")
