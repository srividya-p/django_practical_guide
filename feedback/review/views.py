from django.shortcuts import render, redirect

# Create your views here.

def review(request):
    if request.method == 'POST':
        username = request.POST['username']
        return redirect("/submitted")
        

    return render(request, "review/review.html", {})

def sumbitted(request):
    return render(request, "review/submitted.html", {})
