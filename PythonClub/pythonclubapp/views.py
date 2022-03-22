from django.shortcuts import render, get_object_or_404
from .models import Meeting, Resource
from .forms import MeetingForm,ResourceForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	return render(request, 'pythonclubapp/index.html')

def resources(request):
	resourceList = Resource.objects.all()
	return render(request, 'pythonclubapp/resources.html', {'resourceList': resourceList})

def meetings(request):
	meetingList=Meeting.objects.all()
	return render(request,'pythonclubapp/meetings.html', {'meetingList': meetingList})

def meetingDetails(request,id):
	meeting=get_object_or_404(Meeting,pk=id)
	return render(request,'pythonclubapp/meetingdetails.html', {'meeting': meeting})

##form views
@login_required
def newMeeting(request):
	form=MeetingForm

	if request.method=='POST':
		form=MeetingForm(request.POST)
		if form.is_valid():
			post=form.save(commit=True)
			post.save()
			form=MeetingForm
	else:
		form=MeetingForm()
	return render(request, 'pythonclubapp/newmeeting.html', {'form':form})

@login_required
def newResource(request):
	form=ResourceForm

	if request.method=='POST':
		form=ResourceForm(request.POST)
		if form.is_valid():
			post=form.save(commit=True)
			post.save()
			form=ResourceForm
	else:
		form=ResourceForm()
	return render(request, 'pythonclubapp/newresource.html', {'form':form})

def loginmessage(request):
	return render(request,'pythonclubapp/loginmessage.html')

def logoutmessage(request):
	return render(request,'pythonclubapp/logoutmessage.html')