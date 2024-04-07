from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Room , House
from django.template import loader


def profile(request):
	emil = request.session['member_id']
	user = User.objects.filter(email= email)
	template = loader.get_template('User/index.html')
	context = {
		'User':user,
	}
	return render(request, 'User/profile.html')

def post(request):
	user = request.session['member_id']
	return render(request, 'User/post.html', {'User':user})
