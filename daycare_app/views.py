from django.shortcuts import render
from .forms import BookingForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send email)
            # For now, just print
            print(form.cleaned_data)
            # You can add email sending here
            return render(request, 'contact.html', {'form': BookingForm(), 'success': True})
    else:
        form = BookingForm()
    return render(request, 'contact.html', {'form': form})

def event(request):
    return render(request, 'event.html')

def program(request):
    return render(request, 'program.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')
