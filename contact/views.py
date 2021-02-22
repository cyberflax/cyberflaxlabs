from django.shortcuts import render
from . models import OurContact,contactReq
from service.models import service
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from InspironHome.settings import EMAIL_HOST_USER
from google.googlecontact import upcontact
# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST['txtName']
        email = request.POST['txtEmail']
        Phone = request.POST['txtPhone']
        intrest = request.POST['txtKnow']
        Message = request.POST['txtMessage']
        if intrest == 'others':
            Service = "others"
        else:
            Service = service.objects.get(id = intrest).title
        Contact = contactReq(name = name , email = email , Phone = Phone , intrest = Service , Message = Message)
        Contact.save()
        upcontact(name , Phone , email)
        subject = 'You Have Contact | InspironLabs'
        html_message = render_to_string('contact/email.html', {'name': name , 'phone':Phone , 'email':email , "massage": Message,'intrest': Service})
        plain_message = strip_tags(html_message)
        from_email = EMAIL_HOST_USER
        # to = 'Navneet.cyberflax@gmail.com'
        to = 'ritik.s10120@gmail.com'
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    Contact = OurContact.objects.all()
    res = {
        'title': 'contact',
        'contact' : Contact,
    }
    return render(request, 'contact/contact.html',res)