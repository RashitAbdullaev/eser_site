from django.db import models


class Bid(models.Model):

    name = models.CharField(max_length=25, verbose_name="Имя ученика")
    surname = models.CharField(max_length=25, verbose_name="Фамилия ученика")
    phone_number = models.CharField(max_length=11, verbose_name="Введите свой номер телефона", null=True)
    messages = models.CharField(max_length=200, verbose_name="Что вас интересует", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.phone_number and not self.phone_number.startswith('+'):
            self.phone_number = f'+993{self.phone_number}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Заявки'
        verbose_name = 'Заявка'


class VideoBase(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    video_file = models.FileField(upload_to='media/videos/', verbose_name="Видео")  # Путь к файлу
    image = models.FileField(upload_to='media/videos/photos/', verbose_name="Титульный лист")  # Поле для загрузки изображения

    def __str__(self):
        return self.title

    def delete(self, *args,**kwargs):
        if self.video_file:
            self.video_file.delete(save=False)
        if self.image:
            self.image.delete(save=False)
        super().delete(*args,**kwargs)

    class Meta:
        verbose_name_plural = 'Мероприятия'
        verbose_name = 'Мероприятия'

class Teachers(models.Model):
    name= models.CharField(max_length=250,verbose_name="Имя и фамилия учителя")
    experience = models.IntegerField(verbose_name="Стаж учителя")
    items = models.CharField(max_length=250,verbose_name="Предмет")
    teacher_images = models.FileField(upload_to='media/videos/photos/', verbose_name="Фото учителя")

    def delete(self, *args,**kwargs):
        if self.teacher_images:
            self.teacher_images.delete(save=False)
        super().delete(*args,**kwargs)

    class Meta:
        verbose_name_plural = 'Учителя'
        verbose_name = 'Учитель'

class Cours_category(models.Model):
    category = models.CharField(max_length = 250, verbose_name = "Название направлений")

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Категории курсов'
        verbose_name = 'Категория курсов'

class Course(models.Model):
    course_title = models.CharField(max_length = 250, verbose_name = "Название курса")
    course_description = models.CharField(max_length = 250, verbose_name = "Описание курса")
    course_images = models.FileField(upload_to='media/videos/photos/', verbose_name="Изображение курса")
    category = models.ForeignKey('Cours_category',on_delete = models.PROTECT,verbose_name="Категория курса" )

    def delete(self, *args,**kwargs):
        if self.course_images:
            self.course_images.delete(save=False)
        super().delete(*args,**kwargs)

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'

class Vacancies(models.Model):
    vacancies_title = models.CharField(max_length = 250, verbose_name = "Название вакансии")
    vacancies_experience = models.CharField(max_length=250, verbose_name="Стаж сотрудника")
    vacancies_requirements = models.CharField(max_length=250, verbose_name="Требования к сотруднику")

    class Meta:
        verbose_name_plural = 'Вакансии'
        verbose_name = 'Вакансия'


class Comments(models.Model):
    сomment_description = models.CharField(max_length = 250, verbose_name = "Комментарий")
    comment_name = models.CharField(max_length=250, verbose_name="Имя коментатора")
    comment_avtor = models.CharField(max_length=250, verbose_name="Кто написал комментарий")

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Коментарий'