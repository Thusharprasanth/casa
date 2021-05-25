from django.contrib import messages
from contacts.models import Contact
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
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

# if already made an enquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Alreday made an enqiry for this property')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        # send_mail(
        #     'property listing inquiry',
        #     'there has been a inquiry for' + listing + '. sign into the admin panel for more info.',
        #     'thusharprasanth@gmail.com' ,
        #     [realtor_email],
        #     fail_silently=False,
        # )

        messages.success(request, 'your message has been submitted')

        return redirect('/listings/'+listing_id)