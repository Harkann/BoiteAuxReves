from django.shortcuts import render
from .forms import ReveForm

# Create your views here.
def main_page(request):
    reve_form = ReveForm
    return render(request, 'main/index.html',{"reve_form" : reve_form})
