from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



# def home(request):
#     return HttpResponse("""
#                         <h1>I am coming from Django Server</h1>
#                         <p>lorem34</p>
#                         <br>
#                         <hr>
#                         <p>Hi you are super cool </p>
#                         """)

def home(request):
   
    return render(request,'index.html',context={'page':'Home'})



