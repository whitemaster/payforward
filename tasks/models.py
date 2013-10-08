# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Категория транслитом')
    class Meta:
        verbose_name = 'категорит'
        verbose_name_plural = 'категория'
    def __unicode__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тег')
    name = models.CharField(max_length=100, verbose_name='Тег транслитом')
    class Meta:
        verbose_name = 'теги'
        verbose_name_plural = 'Тег'
    def __unicode__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    end_date = models.DateTimeField(blank=True, verbose_name='Сроки задачи')
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, related_name='tasks')
    tag = models.ForeignKey(Tag, related_name='tasks')
    rate = models.IntegerField(verbose_name='Рейтинг', default=0)
    class Meta:
        verbose_name = 'задачи'
        verbose_name_plural = 'Задача'
    def __unicode__(self):
        return self.title

