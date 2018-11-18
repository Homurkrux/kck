from django.urls import path

from .views import AboutPageView, HomePageView, KekPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('kek/', KekPageView.as_view(), name='kek'),
]
