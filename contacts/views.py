from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        # Get form values
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
        # Save form values on the database
        contact = Contact(listing=listing, listing_id=listing_id, \
            name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # Trigger success message after form submission
        messages.success(request, 'Your request has been submitted. A realtor will get back to you soon!')

        # Redirect to single listing page
        return redirect(f'/listings/{listing_id}')