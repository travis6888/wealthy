import user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import formats
from advisor.forms import EmailUserCreationForm
from wealthy import settings


def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    return render(request, 'profile.html', {})


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            userl = request.user
            text_content = 'Thank you for signing up for our website, {}'.format(userl.username)

            html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our site</div>' \

            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [userl.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("home")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

