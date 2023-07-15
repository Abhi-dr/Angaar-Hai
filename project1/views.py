from django.shortcuts import render


def home(request):
    
    if request.method == "POST":
        uname = request.POST["uname"]
        upassword = request.POST["upassword"]
        
        if uname == "angaar" and upassword == "angaar":
            return render(request, "success.html")
        
        else:
            return render(request, "invalid.html")
    
    return render(request, "home.html")

