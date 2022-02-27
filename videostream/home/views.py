from django.shortcuts import render,redirect,HttpResponse
from home.EmailBackEnd import EmailBackEnd
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from home.models import Video, Category, Comment
from django.views.generic import ListView,CreateView, DetailView, UpdateView, DeleteView
from home.forms import PostVideoForm, EditVideoForm
from django.urls import reverse_lazy, reverse
# Create your views here.



class homeView(ListView):
    model=Video
    template_name='home/home.html'
    ordering=['-created_at']
    
    def get_context_data(self, *args,**kwargs):
        cats_menu=Category.objects.all()
        context=super(homeView, self).get_context_data(*args, **kwargs)
        context['cats_menu']=cats_menu
        return context




class AddPostView(CreateView):
    model=Video
    form_class=PostVideoForm
    template_name='home/add_video.html'



def AddComment(request,pk):
    if request.method=="POST":
        comment=request.POST.get("comment")
        author=request.user
        videoId=request.POST.get("videoId")

        video=Video.objects.get(pk=videoId)
        comment=Comment(body=comment, author=author, video=video)
        comment.save()
        messages.success(request, "your comment has successfully added 🥰")
        return redirect(reverse('Video_Details', args=[str(pk)]))

class VideoDetailsView(DetailView):
    model=Video
    template_name='home/video_details.html'

    def get_context_data(self, *args, **kwargs):
        context=super(VideoDetailsView, self).get_context_data(*args, **kwargs)
        return context
    




class UpdatePostView(UpdateView):
    model=Video
    form_class=EditVideoForm
    template_name='home/update_video.html'

class DeletePostView(DeleteView):
    model=Video
    template_name='home/delete_video.html'
    success_url=reverse_lazy('homeView')

class AddCategoryView(CreateView):
    model=Category
    template_name='home/add_category.html'
    fields='__all__'

def CategoryView(request, cats):
    category_posts=Video.objects.filter(category=cats.replace('_', ' '))
    return render(request, 'home/categories.html',{'cats':cats.replace('_',' ').title(),'category_posts':category_posts})


def CategoryListView(request):
    cats_menu_list=Category.objects.all()
    return render(request, 'home/categories_list.html', {'cats_menu_list':cats_menu_list})






def handleLogin(request):
    if request.method != 'POST':
        return HttpResponse('Submission outside this window is not allowed 😎')
    else:
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user =EmailBackEnd.authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request,"Successfuly logged in 🥰")
            return redirect('homeView')
        else:
            messages.error(request,"Invalid credentials, please try again 😎")
            return redirect('homeView')
    
    
def handleLogout(request):
    if request.method=='POST':
        value=request.POST['value']
        logout(request)
        messages.success(request, "Successfuly logged out 🥰")
        return redirect('homeView')
    else:
        return HttpResponse('Sorry No Users Logged in 😎')   
 
def handelSingup(request):
    if request.method =='POST':
        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        user_exist = User.objects.filter(username=username).exists()
        email_exist = User.objects.filter(email=email).exists()
        if email_exist:
            messages.error(request, "Email Exist!!")
            return redirect('homeView')
        #check for errorneous input
        #username
        else:
            if len(username) > 25:
                messages.error(request, "username is too long(must be less than 26 character)")
                return redirect('homeView')
            if len(username) < 3:
                messages.error(request, "'username is short(must be more than 2 character)")
                return redirect('homeView')
                #password
            if len(pass1) < 8:
                messages.error(request, "Make sure your password is at lest 8 characters")
                return redirect('homeView')
            if len(pass1) > 20:
                messages.error(request, "Make sure your password is under 20 characters")
                return redirect('homeView')
                #pass1 & pass2 should be same
            if pass1 != pass2 :
                messages.error(request, "Password do not match.")
                return redirect('homeView')
            #Create User
            try:
                myuser = User.objects.create_user(username=username, email=email,password=pass1)
                myuser.first_name=fname
                myuser.last_name=lname
                myuser.save()
                messages.success(request, "your account has been successfully created 🥰")
                return redirect('homeView')
            except:
                if user_exist:
                    messages.error(request, "username Exits")
                messages.error(request, "Failed to SignUp!")
                return redirect('homeView')
