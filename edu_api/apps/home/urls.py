from django.urls import path

from home import views

urlpatterns = [
    path("banner/", views.BannerListAPIView.as_view()),
    path("header1/", views.HeaderListAPIView1.as_view()),
    path("header2/", views.HeaderListAPIView2.as_view()),
    path("footer1/", views.FooterListAPIView1.as_view()),
    path("footer2/", views.FooterListAPIView2.as_view()),
]
