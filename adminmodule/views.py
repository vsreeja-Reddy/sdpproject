from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import FeedbackForm
from .models import ContactMessage

# Create your views here.

# Create your views here.
def projecthomepage(request):
    return render(request,'projecthomepage.html')
def aboutus(request):
    return render(request,'aboutus.html')
from django.shortcuts import  render
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request, 'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'projecthomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def signup1(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
        else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render(request,'login.html')
def donate(request):
    return render(request,'donate.html')
def urgent(request):
    return render(request, 'urgent.html')
def animals(request):
    return render(request,'animals.html')
def children(request):
    return render(request,'children.html')
def hungry(request):
    return render(request,'hungry.html')
def disability(request):
    return render(request,'disability.html')
def medical(request):
    return render(request,'medical.html')
def education(request):
    return render(request,'education.html')
def women(request):
    return render(request,'women.html')


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/feedback/')  # Redirect to a success page
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})
# views.py

from django.shortcuts import render, redirect


def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        feedback_text = request.POST['feedback_text']

        feedback_instance = Feedback.objects.create(name=name, email=email, feedback_text=feedback_text)
        messages.success(request, 'Thank you for your feedback!')
        return redirect('/')
    else:
        return render(request, 'feedback.html')

def gallery(request):
    return render(request,'gallery.html')
from django.http import JsonResponse
def donate_now(request):
    return render(request,'donate_now.html')

def children_donate(request):
    return render(request,'children_donate.html')
def animal_donate(request):
    return render(request,'animal_donate.html')

def submit_details(request):
    return render(request,'submit_details.html')

def payment_page(request):
    return render(request,'payment_page.html')
# Assuming you have a DonationForm

from .models import Donation
def process_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            # Retrieve form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            message = form.cleaned_data['message']  # Include message field
            donation_amount = form.cleaned_data['donation_amount']
            donation_frequency = form.cleaned_data['donation_frequency']

            # Create and save Donation object
            Donation.objects.create(
                name=name,
                email=email,
                phone=phone,
                address=address,
                message=message,
                donation_amount=donation_amount,
                donation_frequency=donation_frequency
            )

            # Redirect to a success page or return a response
            return redirect('success_page')  # Replace 'success_page' with your actual success page URL
    else:
        form = DonationForm()

    return render(request, 'donate_now.html', {'form': form})
from django.shortcuts import render
from .models import DonationCard

def donation_cards(request):
    donation_cards = DonationCard.objects.all()
    return render(request, 'donation_cards.html', {'donation_cards': donation_cards})

def contact1(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Create a new ContactMessage object and save it to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Optionally, you can add a success message here
        messages.success(request, 'Message sent successfully!')

        # Redirect the user to the homepage or any other page after successful submission
        return redirect('projecthomepage')  # Change 'projecthomepage' to the correct URL name for your homepage
    else:
        return render(request, 'contact1.html')

