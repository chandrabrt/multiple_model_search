from django.conf.urls import url
from query import views

urlpatterns = [
    url(r'',views.SearchView.as_view(), name='search')
]