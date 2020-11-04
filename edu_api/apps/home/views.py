from rest_framework.generics import ListAPIView

from home.contastnt import BANNER_LENGTH
from home.models import Banner, Nav
from home.serializers import BannerModelSerializer, HeaderModelSerializer


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")[:BANNER_LENGTH]
    serializer_class = BannerModelSerializer


class HeaderListAPIView1(ListAPIView):
    queryset = Nav.objects.filter(position=1, is_site=False)
    serializer_class = HeaderModelSerializer


class HeaderListAPIView2(ListAPIView):
    queryset = Nav.objects.filter(position=1, is_site=True)
    serializer_class = HeaderModelSerializer


class FooterListAPIView1(ListAPIView):
    queryset = Nav.objects.filter(position=2, is_site=False)
    serializer_class = HeaderModelSerializer


class FooterListAPIView2(ListAPIView):
    queryset = Nav.objects.filter(position=2, is_site=True)
    serializer_class = HeaderModelSerializer
