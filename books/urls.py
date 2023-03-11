from django.urls import path
from .views import ListView,DetailsView
app_name='books'
urlpatterns=[

    path('',ListView.as_view(),name='Listview'),
    path('<int:pk>/',DetailsView.as_view(),name='DetailView'),

]

