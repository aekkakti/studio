from django.apps import AppConfig
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from datetime import datetime


class MainConfig(AppConfig):
   verbose_name = 'Дизайнерский сайт'
   name = 'design_studio'

class AdvUser(AbstractUser):
   name = models.CharField(max_length=250, verbose_name="ФИО", help_text="Только кириллические буквы, дефис и пробелы")
   username = models.CharField(max_length=35, verbose_name="Логин", unique=True, help_text="Только латиница и дефис, уникальный")
   is_activated = models.BooleanField(default=True, db_index=True,
                                      verbose_name='Согласен с обработкой '
                                                   'персональных данных?')

class Meta(AbstractUser.Meta):
   pass


class Request(models.Model):
    request_name = models.CharField(max_length=254, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    REQUEST_CATEGORY = (
        ('House', 'House'),
        ('Plane', 'Plane'),
        ('BigBen', 'BigBen'),
    )
    category = models.CharField(
        max_length=10,
        choices=REQUEST_CATEGORY,
        blank=True,
        default='a',
        verbose_name="Категория")
    photo_of_room = models.ImageField(max_length=254, upload_to="media/", verbose_name="Фотография", help_text="Разрешается формата файла только jpg, jpeg, png, bmp",
                                      validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])])
    date_create = models.DateField(default=datetime.now(), verbose_name="Дата создания")
    time_create = models.TimeField(default=datetime.now(), verbose_name="Время создания")
    REQUEST_STATUS = (
        ('Новая', 'Новая'),
    )
    status = models.CharField(
        max_length=6,
        choices=REQUEST_STATUS,
        default='Новая',
        blank=True,
        verbose_name="Статус")


    def __str__(self):
        return self.request_name
