from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

from django.contrib.auth.models import User

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
        
        # Check whether current user id has already made an inquiry for the current listing id
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
        
            if has_contacted:
                # Trigger error message in case there is an inquiry for the current listing
                messages.error(request, 'You have already made an inquiry for this listing!')

                # Redirect to single listing page
                return redirect(f'/listings/{listing_id}')
        
        # Save contact form values on the database
        contact = Contact(listing=listing, listing_id=listing_id, \
            name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # Trigger success message after form submission
        messages.success(request, 'Your request has been submitted. A realtor will get back to you soon!')
        
        # Redirect to single listing page
        return redirect(f'/listings/{listing_id}')