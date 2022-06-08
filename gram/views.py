from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile,Post,Following,Comment
from .forms import DetsForm, PostsForm, CommentsForm
from django.db.models import F
from django.contrib.auth import logout as django_logout
from django.template import RequestContext

def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    posts=Post.objects.all()
    current_user = request.user
    following=Following.objects.filter(username=current_user.username).all()
    followingcount=len(following)
    followers=Following.objects.filter(followed=request.user.username).all()
    followerscount=len(followers)
    if request.method == 'POST':
        form1 = DetsForm(request.POST, request.FILES)
        if form1.is_valid():
            profile = form1.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect('profile')

    else:
        form1 = DetsForm()
    
    return render(request, 'profile.html', {"form1":form1,"posts":posts,"followingcount":followingcount,"followerscount":followerscount})

@login_required(login_url='/accounts/login/')
def post(request):
    if request.method == "POST":
        form2=PostsForm(data=request.POST,files=request.FILES)
        if form2.is_valid():
            form2.save()
            obj=form2.instance
        return redirect(request,"main",{"obj":obj})
    else:
          form2=PostsForm()
          img=Post.objects.all()
    return render(request,"newpost.html",{"img":img,"form":form2})

@login_required(login_url='/accounts/login/')
def main(request):
    users = User.objects.all()
    posts = Post.objects.all()
    follows = Following.objects.all()
    comments = Comment.objects.all()
    if request.method=='POST' and 'follow' in request.POST:
        following=Following(username=request.POST.get("follow"),followed=request.user.username)
        following.save()
        return redirect('main')
    elif request.method=='POST' and 'comment' in request.POST:
        comment=Comment(comment=request.POST.get("comment"),
                        post=int(request.POST.get("posted")),
                        username=request.POST.get("user"),
                        count=0)
        comment.save()
        comment.count=F('count')+1
        return redirect('main')
    elif request.method=='POST' and 'post' in request.POST:
        posted=request.POST.get("post")
        for post in posts:
            if (int(post.id)==int(posted)):
                post.like+=1
                post.save()
        return redirect('main')
    else:
        return render(request, 'main.html',{"users":users,"follows":follows,"posts":posts,"comments":comments})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = DetsForm(request.POST, request.FILES)
        if form.is_valid():
                Profile.objects.filter(id=current_user.profile.id).update(bio=form.cleaned_data["bio"])
                profile = Profile.objects.filter(id=current_user.profile.id).first()
                profile.profile_pic.delete()
                profile.profile_pic=form.cleaned_data["profile_pic"]
                profile.save()
        return redirect('profile')

    else:
        form = DetsForm()
    
    return render(request, 'edit_profile.html',{"form": form})

@login_required(login_url='/accounts/login/')
def search(request):
    posts=Post.objects.all()
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        following=Following.objects.filter(username=search_term).all()
        followingcount=len(following)
        followers=Following.objects.filter(followed=search_term).all()
        followercount=len(followers)
        searched_user = User.objects.filter(username=search_term).first()
        if searched_user:
            message = f"{search_term}"
            return render(request, 'search_results.html',{"profile_user": searched_user,"posts":posts,"followingcount":followingcount,"followercount":followercount})
        else:
            message = "The username does not exist."
            return render(request, 'error.html',{"message":message})

@login_required(login_url='/accounts/login/')
def comment(request):
    post = Post.objects.all()
    comments = post.comments.get(active=True)

    if request.method == 'POST':
        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentsForm()                   
    return render(request, 'post_detail.html',{'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})

@login_required(login_url='/accounts/login/')
def logout(request):
    django_logout(request)    
    return render(request, 'welcome.html')
