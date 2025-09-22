from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва кафедри")
    head = models.CharField(max_length=100, verbose_name="Завідувач кафедри")
    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва спеціальності", default="не вказано")
    code = models.CharField(max_length=10, verbose_name="Код спеціальності", default="не вказано")
    description = models.TextField(verbose_name="Опис", default="не вказано")
    coordinator_name = models.CharField(max_length=100, verbose_name="Імʼя координатора набору", default="не вказано")
    coordinator_contact = models.CharField(max_length=100, verbose_name="Контакт координатора набору", default="не вказано")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="programs", verbose_name="Випускова кафедра", null=True, blank=True)
    disciplines = models.TextField(verbose_name="Список дисциплін (через кому)", default="не вказано")
    def __str__(self):
        return f"{self.code} {self.name}"

class Lecturer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Імʼя")
    position = models.CharField(max_length=100, verbose_name="Посада")
    degree = models.CharField(max_length=100, verbose_name="Ступінь")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="lecturers", verbose_name="Кафедра")
    def __str__(self):
        return self.name

class HomePageContent(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    def __str__(self):
        return self.title
