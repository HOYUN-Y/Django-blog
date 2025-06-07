from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from . import models
from .forms import PostForm, GuestbookEntryForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import FileResponse
from django.utils.encoding import smart_str
from urllib.parse import quote
import os

# Create your views here.
def landing_view(request):
    if not request.session.get('visited_profile'):
        request.session['visited_profile'] = True
        return redirect('blog:profile_first')
    return redirect('home')


#프로필 페이지 ?
def profile(request):
    return render(request,'blog/profile.html', {'hide_nav':False})


def profile_first(request):
    return render(request,'blog/profile.html', {'hide_nav':True})

def home(request):
    recent_posts = models.Posts.objects.all().order_by('-created_time')[:3]

    context={'recent_posts':recent_posts}
    return render(request, 'blog/home.html', context=context)



def post_list(request):
    all_posts = models.Posts.objects.all().order_by('-created_time')   
    search_kwd = ''
    post_type = request.GET.get('type')
    if post_type:
        all_posts = models.Posts.objects.filter(type=post_type).order_by('-created_time')

    if request.method == "POST":
        search_kwd = request.POST.get('search','')
        if search_kwd:
            all_posts = models.Posts.objects.filter(Q(title__icontains=search_kwd) | Q(content__icontains=search_kwd))
                 
    context = {'all_posts':all_posts, 'search_kwd':search_kwd}

    return render(request, 'blog/post_list.html', context=context)

def post_detail(request, pk):
    post = get_object_or_404(models.Posts, pk=pk)
    prev_post = models.Posts.objects.filter(created_time__lt=post.created_time).order_by('-created_time').first()
    next_post = models.Posts.objects.filter(created_time__gt = post.created_time).order_by('created_time').first()

    context={'prev_post':prev_post, 'next_post':next_post, 'post' : post}
    return render(request, 'blog/post_detail.html', context=context)


def list_portfolio(request):
    all_projects = models.Posts.objects.filter(type='portfolio')
    return render(request, 'blog/portfolio_list.html',{'all_projects':all_projects})


#이력서 페이지? 
def resume(request):
    return render(request, 'blog/resume.html')


def settings(request):
    return render(request, 'blog/settings.html')


#post등록
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:list')
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form':form})


#게시글 삭제
def delete_post():
    pass



#자료실
def documents(request):
    documents = models.Document.objects.all().order_by('-uploaded_time')
    context = {'documents':documents}
    return render(request, 'blog/documents.html', context = context)


def download_document(request, document_id):
    doc = get_object_or_404(models.Document, pk=document_id)
    file_path = doc.file.path
    response = FileResponse(open(file_path,'rb'))
    filename = quote(doc.original_filename)
    response['Content-Disposition'] = f"attachment; filename*=UTF-8''{filename}"
    return response

#statements page
def statement_list(request):
    all_statements = models.Statements.objects.all()

    return render(request, 'blog/statement_list.html',{'all_statements':all_statements})

def statement_detail(request, pk):
    statement = get_object_or_404(models.Statements, pk=pk)
    context = {'post':statement}
    #return render(request, 'blog/post_detail.html', context=context)
    return render(request, 'blog/statement_detail.html', context=context)


#방명록
def guestbook(request):
    entries = models.GuestbookEntry.objects.order_by('-created_at')
    form = GuestbookEntryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('blog:guestbook')
    paginator = Paginator(entries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'form' : form, 
               'entries' : page_obj,
               }
    return render(request, 'blog/guestbook.html' ,context=context)
