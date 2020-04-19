from django.shortcuts import render
from django.views.generic.base import View

from promotions.models import Banner


class BannerView(View):
    def get(self, request):
        # 取出轮播图
        all_banners = Banner.objects.all().order_by('index')
        return render(request, 'index.html', {
            'all_banners': all_banners,
        })


