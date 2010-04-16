# Create your views here.

from models import Note
from django.http import HttpResponseRedirect, HttpResponseServerError

def create_note(request):
	error_msg = u"No POST data sent."
	if request.method == "POST":
		post = request.POST.copy()
		if post.has_key('slug') and post.has_key('title'):
			slug = post['slug']
			if Note.objects.filter(slug=slug).count() > 0:
				error_msg = u"Slug already in use."
			else:
				title = post['title']
				new_note = Note.objects.create(title=title , slug=slug)
				return HttpResponseRedirect(new_note.get_absolute_url())
		else:
			error_msg = u"Insufficient POST data (need 'slug' and 'title'!)"
	
	return HttpResponseServerError(error_msg)

	
def update_note(request , slug):
	if request.method == "POST":
		post = request.POST.copy()
		note = Note.objects.get(slug = slug) #Should possibly catch case where slug is invalid
		if post.has_key('slug'):
			slug_str = post['slug']
			if not(slug == slug_str) and Note.objects.filter(slug = slug_str).count() > 0:
				error_msg = u"Slug %s already taken." %slug_str
				return HttpResponseServerError(error_msg)
				
			note.slug = slug_str
		
		if post.has_key('title'):
			note.title = post['title']
		
		if post.has_key('text'):
			note.text = post['text']
		
		note.save()
		return HttpResponseRedirect('/')
	
	error_msg = u"No POST data sent"
	return HttpResponseServerError(error_msg)

	
	
