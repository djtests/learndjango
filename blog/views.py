from django.core.mail import send_mail
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models	 import Blog
from .forms import EmailPostForm
# Create your views here.

# Funtion base view

#1 URL request 
#2. Map the corresponding view funtions  (handler)
#3. Generate the response
# 3.1 template
# 3.2 model (data)

def home(request):
	# Number of visits to this view, as counted in the session variable.
	num_visits=request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits+1
	
	num_blogs = Blog.objects.all().count
	# num_authors =Author.objects.all().count
	num_authors = 5
	
	context={'num_blogs':num_blogs,'num_authors':num_authors, 'num_visits':num_visits}
	
	return render(request,'index.html',context)

def author(request):
	return HttpResponse("Authors")


# def blog_list(request):
#        posts = Blog.objects.all()
#        return render(request,
#                      'index.html',
#                      {'posts': posts})

def blog_detail(request,pk):
	# try:
	# 	post=Blog.objects.get(pk=pk)
	# except Blog.DoesNotExist:
	# 	raise Http404("Blog does not exist")
		
	post=get_object_or_404(Blog, pk=pk)
	return render(
        request,
        'blog/blog_detail.html',
        context={'post':post,}
    )

class BlogListView(generic.ListView):
	posts = Blog
	context_object_name= 'posts'
	queryset = Blog.objects.all()
	template_name = 'blog/blog_list.html'
	paginate_by = 1

class BlogDetailView(generic.DetailView):
	pass



# This view works as follows:
# • We define the post_share view that takes the request object and the
# post_id as parameters.
# • We use the get_object_or_404() shortcut to retrieve the post by ID and
# make sure the retrieved post has a published status.
# • We use the same view for both displaying the initial form and processing the submitted data. 
# We differentiate if the form was submitted or not based on the request method. 
# We are going to submit the form using POST. We assume that if we get a GET request, an empty form has to be displayed, and if we get a POST request, the form was submitted and needs to be processed. Therefore, we use request.method == 'POST' to distinguish between the two scenarios.
def post_share(request,pk):
	# Retrieve post by id
	post = get_object_or_404(Blog, id=pk, status='publish')
	sent = False

	if request.method == 'POST':
		# Form was submitted
		form = EmailPostForm(request.POST)
		if form.is_valid():
			# Form fields passed validation
			cd = form.cleaned_data
			# ... send email
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
			message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
			send_mail(subject, message, 'bprajyotan@gmail.com',[cd['to']])
			sent = True
	else:
		form = EmailPostForm()
			
	return render(request, 'blog/share.html', {'post': post,
												'form': form,
												'sent':sent})
