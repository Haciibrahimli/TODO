from django.shortcuts import render

def index_view(request):
    contex = {

    }
    
    return render(request,"index.html",contex )
    
