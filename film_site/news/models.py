from django.db import models


# Create your models here.
class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.CharField('Имя пользователя', max_length=50)

    def __str__(self):
        return self.title

    def get_full_info(self):
        return (
            f"Название: {self.title}\n"
            f"Краткое описание: {self.short_description}\n"
            f"Текст новости: {self.text}\n"
            f"Дата публикации: {self.pub_date}\n"
            f"Автор: {self.author}"
        )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


