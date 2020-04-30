#I have created this file-Rahul
from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
 #   return HttpResponse("Rahul Mere  Bhai Kaisa Hai")
#def about(request):
 #   return HttpResponse('''<h1>About Rahul<h1><a href="www.fb.com">Rahul Bhaiya</a>''')

#def index(request):
  #  return render(request, 'index.html')

    # return HttpResponse("Home")
#def removepunc(request):
#    djtext=request.GET.get("text","default")#get the text
 #   print(djtext)#analyze the text
  #  return HttpResponse("remove punctuation")
#def capfirst(request):
#    return HttpResponse("capitalize first")
#def newlineremove(request):
 #   return HttpResponse("new line remove")
#def spaceremove(request):
 #   return HttpResponse("space remove")
#def charcount(request):
 #   return HttpResponse("character count")

def index(request):
     return render(request, 'index.html')

     #return HttpResponse("Home")
def analyze(request):
    #djtext=request.GET.get("text","default")#get the text
     djtext=request.POST.get("text","default")
     print(djtext)
     removepunc=request.POST.get("removepunc","off")
     fullcaps=request.POST.get("fullcaps","off")
     newlineremove=request.POST.get("newlineremove","off")
     spaceremove=request.POST.get("spaceremove","off")
     #print(removepunc)
    #analyze the text
     if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
    #return HttpResponse("remove punctuation")
        djtext=analyzed
        #return render(request,'analyze.html',params)
     if(fullcaps=="on"):
       
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Change to Uppercase','analyzed_text':analyzed}
        djtext=analyzed   
        #return render(request,'analyze.html',params)
     if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        #return render(request,'analyze.html',params)
        
     if(spaceremove=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

        
     if(removepunc!="on" and fullcaps!="on" and newlineremove!="on" and spaceremove!="on"):
         return HttpResponse("please select the operation")
        #return render(request,'analyze.html',params)
   # elif(charcount=="on"):
    #    analyzed=djtext
        
     #   params={'purpose':'Character Count','analyzed_text':analyzed}
    
      #  return render(request,'analyze.html',params)
    
     return render(request,'analyze.html',params)
def aboutus(request):
     return render(request, 'aboutus.html')
def contactus(request):
     return render(request, 'contactus.html')
