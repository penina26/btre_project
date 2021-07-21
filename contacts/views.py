from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #check  if user has made iquiry already

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already submitted an inquiry for this listing')

            return redirect('/listings/'+listing_id)




        contact = Contact(listing_id=listing_id, listing=listing,name=name,
        email=email,phone=phone,message=message,user_id=user_id,)

        contact.save()

        #Send email

        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
            'ruthnaliaka34@gmail.com',
            [realtor_email,'wpenina@gmail.com'],
            fail_silently=False
        )




        messages.success(request,'You request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)

       
            
