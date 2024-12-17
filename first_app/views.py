from django.shortcuts import render
from .forms import FormClass
# Create your views here.
def home(request):
    return render(request, 'home.html')

def form_api(request):
    return render(request, 'form_api.html')


def submitFormApi(request):
    if request.method== "POST":
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        email = request.POST.get('email')
        agree = request.POST.get('agree')
        birth_date = request.POST.get('birth_date')
        birth_year = request.POST.get('birth_year')
        value = request.POST.get('value')
        email_address = request.POST.get('email_address')
        message = request.POST.get('message')
        first_name = request.POST.get('first_name')
        day = request.POST.get('day')
        favorite_colors = request.POST.getlist('favorite_colors')
        return render(request, 'show.html', {'name': name, 'comment': comment, 'email': email, 'agree': agree, 'birth_date': birth_date, 'birth_year': birth_year, 'value': value, 'email_address': email_address, 'message': message, 'first_name': first_name, 'day': day, 'favorite_colors': ', '.join(favorite_colors)})

    else:
        return render(request, 'show.html')


def djangoForm(request):
    form= FormClass(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'django_form.html', {'form': form})


# def submitDjangoForm(request):

