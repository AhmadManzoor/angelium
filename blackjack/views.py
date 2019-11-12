from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import BJ_history
from django.template import loader
from django.urls import reverse
# Create your views here.

def index(request):
	history=BJ_history.objects.order_by('time')
	template=loader.get_template('blackjack/index.html')
	context={
		'history' : history,
	}
	return HttpResponse(template.render(context,request))

def details(request, id):
	data=get_object_or_404(BJ_history,pk=id)
	return render(request,'blackjack/detail.html',{'data':data})
	# try:
	# 	data=BJ_history.objects.get(pk=id)
	# except data.DoesNotExist as e:
	# 	raise Http404('Data related to this game do not exist')
	# return render(request,'blackjack/detail.html',{'data':data})

def choice(request,id):
	get_object_or_404(BJ_history,pk=id)
	