from django.shortcuts import render
from .models import contact,Feedback

# Create your views here.
def Home(request):
    return render(request,'home.html')

def contacts(request):
    if request.method=='GET':
        return render(request,'contact.html')
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')

        contact(
            name=name,
            email=email,
            query=query
        ).save()
        return render(request, 'contact.html')


def services (request):
    return render(request,'services.html')

def feedback(request):
    if request.method=='GET':
        feedbacks=Feedback.objects.all()
        return render(request,'feedback.html',{'feedbacks':feedbacks})
    else:
        name=request.POST.get('name')
        feedback=request.POST.get('feedback')

        Feedback(
            name=name,feedback=feedback
        ).save()
        feedbacks = Feedback.objects.all()
        return render(request, 'feedback.html',{'feedbacks':feedbacks})


def gallery(request):
    return render(request,'gallery.html')
