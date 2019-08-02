from django.shortcuts import render
from django.utils import timezone
from .models import Message
# Create your views here.
def post_list(request):
    posts = Message.objects.order_by('published_date')
    return render(request, 'show/post_list.html',  {'posts': posts})