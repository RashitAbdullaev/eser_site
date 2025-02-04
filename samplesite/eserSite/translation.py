from modeltranslation.translator import translator, TranslationOptions
from .models import VideoBase,Teachers,Cours_category,Course,Vacancies

class VideoBaseTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class TeachersTranslationOptions(TranslationOptions):
    fields = ('name', 'items')

class Cours_categoryTranslationOptions(TranslationOptions):
    fields = ('category',)

class CourseTranslationOptions(TranslationOptions):
    fields = ('course_title', 'course_description')

class VacanciesTranslationOptions(TranslationOptions):
    fields = ('vacancies_title', 'vacancies_experience','vacancies_requirements',)

translator.register(VideoBase, VideoBaseTranslationOptions)
translator.register(Teachers, TeachersTranslationOptions)
translator.register(Cours_category, Cours_categoryTranslationOptions)
translator.register(Course,CourseTranslationOptions)
translator.register(Vacancies,VacanciesTranslationOptions)