
from django.urls import path,include
from .views import(
    HomeView,
    AboutUsView,
    GalleryView,
    ProgramView,
    ContributeView,
    ContactUsView,
    postDonation,
    postMessage,
    ProgramDetailView,
) 

app_name = 'core'

urlpatterns = [
    # path('', HomeView.as_view(),name='home'),
    path('', HomeView, name='home'),
    path('about-us/', AboutUsView, name='about-us'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('contact/', postMessage.as_view(), name='contact'),
    path('donation/', postDonation.as_view(), name='donation'),
    path('program-list/', ProgramView, name='program-list'),
    path('details/<int:pk>/', ProgramDetailView, name='details'),
    path('contribute/', ContributeView, name='contribute'),
    path('contact-us/', ContactUsView, name='contact-us'),
]