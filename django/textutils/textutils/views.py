# views.py

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def aboutus(request):
    return render(request, "aboutus.html")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Initialize the params dictionary with default values
    params = {'purpose': '', 'analyzed_text': djtext}

    # Check if no transformations are selected
    if removepunc == fullcaps == newlineremover == extraspaceremover == 'off':
        params['purpose'] = 'Please select at least one option'
        params['analyzed_text'] = 'Please enable at least one transformation option.'
    else:
        analyzed = djtext  # Initialize analyzed text with the input text

        if removepunc == "on":
            # Remove punctuations
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ''.join(char for char in analyzed if char not in punctuations)
            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}

        if fullcaps == "on":
            # Convert to uppercase
            analyzed = analyzed.upper()
            params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}

        if newlineremover == "on":
        # Remove newlines only if the "new line remover" function is enabled
            analyzed = analyzed.replace('\n', ' ')
            params['purpose'] = 'Removed NewLines'
            params['analyzed_text'] = analyzed
        else:
            params['purpose'] = 'Analysis without New Line Remover'  # Set a purpose for the analysis without newline removal

        if extraspaceremover == "on":
            # Remove extra spaces
            analyzed = ' '.join(analyzed.split())
            params = {'purpose': 'Extra Space Is Removed', 'analyzed_text': analyzed}

    return render(request, 'analyze.html', params)
