from django.shortcuts import render

from .models import Mother

def mother(request):
	content = ''
	if request.method == 'POST':
		content = request.POST.get('content')
		Mother.objects.create(content=content)
	return render(request, 'polls/mother.html', {'content': content})
