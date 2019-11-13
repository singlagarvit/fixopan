from django.shortcuts import render, redirect

def home_view(request):
	return render(request, 'index.html', {})

def about_view(request):
	return render(request, 'about.html', {})

def advantages_view(request):
	return render(request, 'advantages.html', {})

def waterstop_view(request):
	return render(request, 'waterstop.html', {})

def profiles_view(request):
	return render(request, 'profiles.html', {})

def contruction_view(request):
	return render(request, 'construction-joints.html', {})