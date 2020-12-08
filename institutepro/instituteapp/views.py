from django.shortcuts import render
from.models import ContactData
from.models import FeedbackData
import datetime
date = datetime.datetime.now()

def home_page(request):
    return render(request,'instituteapp/home.html')

#def contact_page(request):
    #return render(request,'instituteapp/contact.html')

def contact_view(request):
    if request.method=="GET":
        return render(request,'instituteapp/contact.html')
    else:
        ename1 = request.POST.get('ename')
        email1 = request.POST.get('email')
        address1 = request.POST.get('address')
        contact1 = request.POST.get('contact')
        course1 = request.POST.get('course')

        data = ContactData(
            name = ename1,
            email = email1,
            address = address1,
            contact = contact1,
            course = course1
        )
        data.save()
        return render(request,'instituteapp/contact.html')


def gallery_page(request):
    return render(request,'instituteapp/gallery.html')

def courses_page(request):
    return render(request,'instituteapp/courses.html')

def feedback_page(request):
    if request.method=="POST":
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        feedback = request.POST.get('feedback')

        data = FeedbackData(
            name=name,
            rating=rating,
            date=date,
            feedback=feedback
        )
        data.save()
        feedbacks = FeedbackData.objects.all()
        return render(request,'instituteapp/feedback.html',{'feedback':feedbacks})
    else:
        feedbacks = FeedbackData.objects.all()
        return render(request,'instituteapp/feedback.html',{'feedback':feedbacks})