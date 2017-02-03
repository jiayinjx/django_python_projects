from django.shortcuts import render, redirect ,get_object_or_404
from .models import Article, Comment, Poll, NewUser
from .forms import CommentForm, LoginForm, RegisterForm, SetInfoForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout #(the 3 ways to check the system settings)
from django.http import JsonResponse
from django.views.decorators.cache import cache_page

import markdown2
from urllib.parse import urlparse

def index(request):
	latest_article_list = Article.objects.query_by_time() 
		# need to add ArticleManager in models.py
	loginform = LoginForm()
	content = {'latest_article_list': latest_article_list, 'loginform': loginform}
	return render(request, 'index.html', content)
		# means the user access to the website from index.html
		# to find the index.html, have to add tempates category in settings.py: change 'DIR':[]


# for Log in and Log out:
def log_in(request):
	if request.method =="GET":
		form = LoginForm()
		return render(request, 'login.html', {'form': form})
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.IS_VALID():
			username = form.cleaned_data['uid']
			password = form.cleaned_data['pwd']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				url = request.POST.get('source_url', '/focus')
				return redirect(url)
			else:
				return render(rquest, 'login.html', {'form': form, 'error': "password or username is not ture!"})

		else:
			return render(request, 'login.html', {'form': form})

@login_required
# @login_required is a decorator in django. ，它的作用是使所装饰的函数必须是登录的用户才继续运行，不然进入指定的login_url
def log_out(request):
	url = request.POST.get('source_url', './focus/')
	logout(request)
	return redirect(url)


def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    content = mardown2.markdown(article.content, extras=["code-friendly", "fenced-code-blocks", "header-ids", "toc", "metadata"])
    commentform = CommentForm()
    loginform = LoginForm()
    comments = article.comment_set.all

    return render(request, 'article_page.html', {
    	'article': article,
    	'loginform': loginform,
    	'commentform': commentform,
    	'content': content,
    	'comments': comments
    	})

@login_required
def comment(request, article_id):
	form = CommentForm(request.POST)
	url = urlparse.urljoin('/focus/', article_id)
	if form.is_valid():
		user = request.user
		article = Article.objects.get(id=article_id)
		new_comment = form.cleaned_data['comment']
		c = Comment(content=new_comment, article_id=article_id) # have tested by shell
		c.user = user
		c.save()
		article.comment_nums += 1
	return redirect(url)

@login_required
def get_keep(request, article_id):
	logged_user = request.user
	article = Article.objects.get(id=article_id)
	articles = logged_user.article_set.all() # using related objects reference 
	if article not in articles:
		article.user.add(logged_user) # for m2m linking, have tested by shell
		article_keep_num += 1
		article.save()

		return redirect('/focus/')
	else:
		url = urlparse.urljoin('/focus/', article_id)
		return redirect(url)

@login_required
def get_poll_article(request, article_id):
	logged_user = request.user
	article = Article.objects.get(id=article_id)
	polls = logged_user.poll_set.all()
	articles = []
	for poll in polls:
		articles.append(poll.article)

	if article in articles:
		url = urlparse.urljoin('/focus/', article_id)
		# urlparse.urljoin() in python function that used for joint url
		return redirect(url)
	else:
		article.poll_num += 1
		article.save()
		poll = Poll(user=logged_user, article=article)
		poll.save()
		data = {}
		return redirect('/focus/')


# sign up a new user:
def register(request):
	# use forms to show the 2 error message since it has them.
	error1 = "this name is already exist"
	#error2 = "two password is not equal"
	valid = "this name is valid"

	if request.method == 'GET':
		form = RegisterForm()
		return render(request, 'register.html', {'form': form})
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		# 2 ways to get POST:
		# 1)AJAX send post 
		if request.POST.get('raw_username', 'erjgiqfv240hqp5668ej23foi') != 'erjgiqfv240hqp5668ej23foi':  # if ajax
			try:
				user = NewUser.objects.get(username=request.POST.get('raw_username',''))
			except ObjectDoesNotExist:
				return render(request, 'register.html', {'form': form, 'msg': valid})
			else:
				return render(request, 'register.html', {'form': form, 'msg': error1})

		# 2) user click the register button
		else:
			if form.is_valid():
				username = form.cleaned_data['username']
				email = form.cleaned_data['email']
				password1 = form.cleaned_data['password1']
				password2 = form.cleaned_data['password2']
				if password1 != password2:
					return render(request, 'register.html', {'form': form, 'msg': "two password is not equal"}) # or use error2
				else:
					user = NewUser(username=username, email=email, password=password1)
					user.save()
					# return render(request, 'login.html', {'success': "you have successfully registered!"})
					return redirect('/focus/login')
			else:
				return render(request, 'register.html', {'form': form})
