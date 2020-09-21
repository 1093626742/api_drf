

from django.urls import path,re_path
from  . import views
urlpatterns = [
    path('book',views.BookView.as_view()),
    re_path(r'book/(?P<pk>\d+)',views.BookDetailView.as_view()),
]
