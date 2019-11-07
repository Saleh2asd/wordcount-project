from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html', {"dectionsorse" : "This is from dictionary"})

def count(request):
    fulltext = request.GET['fulltext']
    
    wordcount = fulltext.split()
    
    worddictionary = {}
    
    for word in wordcount:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    
    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)
    
    return render(request, 'count.html', {'x':fulltext, 'y':len(wordcount), 'z':sortedwords})

def hi(request):
    return HttpResponse('<h1>Hi</h1>')
def about(request):
    return render(request, 'about.html', {"here" : "This is the 1st challange"})