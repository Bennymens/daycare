from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            contact_data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'address': form.cleaned_data['address'],
                'message': form.cleaned_data['message']
            }

            # Email sending commented out for now
            # Send confirmation email to user
            # user_subject = 'Booking Confirmation - Little Lamb Babysitting'
            # user_message = render_to_string('email/user_confirmation.html', {
            #     'contact': contact_data,
            # })

            # try:
            #     send_mail(
            #         user_subject,
            #         '',  # Plain text version (empty for HTML)
            #         'littlelambbabysitting01@gmail.com',
            #         [contact_data['email']],
            #         html_message=user_message,
            #         fail_silently=False,
            #     )
            # except Exception as e:
            #     print(f"Error sending user email: {e}")

            # Send notification email to admin
            # admin_subject = f'New Booking Request from {contact_data["name"]}'
            # admin_message = render_to_string('email/admin_notification.html', {
            #     'contact': contact_data,
            # })

            # try:
            #     send_mail(
            #         admin_subject,
            #         '',  # Plain text version (empty for HTML)
            #         'littlelambbabysitting01@gmail.com',
            #         ['littlelambbabysitting01@gmail.com'],
            #         html_message=admin_message,
            #         fail_silently=False,
            #     )
            # except Exception as e:
            #     print(f"Error sending admin email: {e}")

            # Redirect with success message (simple redirect for now)
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def page_404(request):
    return render(request, '404.html')
