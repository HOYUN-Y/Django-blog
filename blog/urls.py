from django.urls import path, include
from . import views


app_name='blog'

urlpatterns=[
    path('home/',views.home,name='home'),
    path('profile/first/', views.profile_first, name='profile_first'),
    path('list/', views.post_list, name='list'),
    path('list_portfolio/', views.list_portfolio, name='list_portfolio'),
    path('resume/', views.resume, name="resume"),
    path('settings/', views.settings, name="settings"),
    path('create/',views.create_post, name='create'),
    path('detail/<int:pk>',views.post_detail, name='detail'),
    path('documents/',views.documents, name='documents'),
    path('profile/',views.profile, name='profile'),
    path('statement_detail/<int:pk>', views.statement_detail, name='statement_detail'),
    path('list_statements/', views.statement_list, name='list_statements'),
    path('guestbook/',views.guestbook, name='guestbook'),
    path('documents/download/<int:document_id>/', views.download_document, name='download_document'),
    
]