from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .form import CustomFileFirm
from .models import *


class BidAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "surname", "phone_number", "messages")
    list_display_links = ("pk", "name", "surname", "phone_number", "messages")


class VideBaseAdmin(TranslationAdmin):
    list_display = ("pk", "title", "description", "video_file", "image")
    list_display_links = ("pk", "title", "description", "video_file", "image")

class TeachersAdmin(TranslationAdmin):
    list_display = ("pk", "name", "experience", "items", "teacher_images")
    list_display_links = ("pk", "name", "experience", "items", "teacher_images")

class Cours_categoryAdmin(TranslationAdmin):
    list_display = ("pk", "category",)
    list_display_links = ("pk", "category",)

class CourseAdmin(TranslationAdmin):
    list_display = ("pk", "course_title", "course_description", "course_images", "category")
    list_display_links = ("pk", "course_title", "course_description", "course_images", "category")


class VacanciesAdmin(TranslationAdmin):
    list_display = ("pk", "vacancies_title", "vacancies_experience", "vacancies_requirements")
    list_display_links = ("pk", "vacancies_title", "vacancies_experience", "vacancies_requirements")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "сomment_description", "comment_name", "comment_avtor",)
    list_display_links = ("pk", "сomment_description", "comment_name", "comment_avtor",)

admin.site.register(Bid, BidAdmin)
admin.site.register(VideoBase, VideBaseAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Cours_category, Cours_categoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Vacancies, VacanciesAdmin)
admin.site.register(Comments, CommentAdmin)
