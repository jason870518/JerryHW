from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import Introduction
# Create your views here.
def index(request):
	introdutions = Introduction.objects.all()
	return render_to_response('jason/menu.html', locals())