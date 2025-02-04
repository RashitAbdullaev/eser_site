from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import *
from django.views.generic import ListView, CreateView
from .form import *


class ListSite(ListView):
    model = Bid
    template_name = 'eserSite/mainPage.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.all()
        return context


class LanguagePage(ListView):
    model = Course

    def get_template_names(self):
        if self.request.path == '/':
            return ['eserSite/mainPage.html']
        elif self.request.path == '/england':
            return ['eserSite/EnglandPage.html']
        elif self.request.path == '/germany':
            return ['eserSite/GermanyPage.html']
        elif self.request.path == '/chine':
            return ['eserSite/ChinePage.html']
        elif self.request.path == '/russia':
            return ['eserSite/RussiaPage.html']
        elif self.request.path == '/komp':
            return ['eserSite/KompPage.html']
        elif self.request.path == '/vacancies':
            return ['eserSite/vacancies.html']
        return ['eserSite/MathPage.html']


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lets_go'] = Course.objects.filter(category=1)
        context['english_file'] = Course.objects.filter(category=2)
        context['headway'] = Course.objects.filter(category=3)
        context['ielts'] = Course.objects.filter(category=4)
        context['german'] = Course.objects.filter(category=5)
        context['komp_teh'] = Course.objects.filter(category=6)
        context['design'] = Course.objects.filter(category=7)
        context['web_design'] = Course.objects.filter(category=8)
        context['big_matem'] = Course.objects.filter(category=9)
        context['sat_matem'] = Course.objects.filter(category=10)
        context['rus_little'] = Course.objects.filter(category=11)
        context['rus_big'] = Course.objects.filter(category=12)
        context['chine_big'] = Course.objects.filter(category=13)
        context['physics'] = Course.objects.filter(category=14)
        context['vacancies'] = Vacancies.objects.all()
        return context

class TeacherInfo(ListView):
    model = Bid
    template_name = 'eserSite/TeacherInfo.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_all'] = Teachers.objects.all()
        return context


class BidCreate(CreateView):
    template_name = 'eserSite/BidCreate.html'
    form_class = BidForm
    success_url = reverse_lazy('eserSite:main_page')


class VideoList(ListView):
    model = VideoBase
    template_name = 'eserSite/VideoList.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_all'] = VideoBase.objects.all()
        return context


class VideoSingle(ListView):
    model = VideoBase
    template_name = 'eserSite/VideoSingle.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_single'] = VideoBase.objects.filter(pk=self.kwargs['pk'])
        context['video_all'] = VideoBase.objects.exclude(pk=self.kwargs['pk'])
        return context




