from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordDict = {}
    for word in wordlist:
        if word in wordDict:
            wordDict[word] = wordDict[word]+1
        else:
            wordDict[word] = 1
    
    def takeSecond(elem):
        return elem[1]
    
    tempList = []
    for key, value in wordDict.items():
        temp = (key, value)
        tempList.append(temp)
    tempList.sort(key=takeSecond, reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'wordDict':tempList})

def about(request):
    return render(request, 'about.html')