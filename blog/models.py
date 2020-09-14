from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    '''Категория блога'''
    title = models.CharField('title', max_length=50)

    class Meta: 
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    '''Тег блога'''
    title = models.CharField('title', max_length=50)

    class Meta: 
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.title    


class Blog(models.Model):
    '''Модель блога, который может создать каждый пользователь'''
    topic = models.CharField('topic', max_length=50)
    subtitle = models.CharField('subtitle', max_length=150)
    text = models.TextField('text', max_length=5000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    img = models.ImageField('Main image of your blog', upload_to='blog')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.topic

    class Meta: 
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'


class Gallery(models.Model):
    '''Галерея фотографий для блога'''
    img = models.ImageField('Subimage in your blog', upload_to='gallery')
    description = models.CharField('Description of the image', max_length=50)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'


class Review(models.Model):
    '''Отзыв статьи, чтобы можно было вести беседу на тему блога'''
    text = models.TextField('text of message', max_length=5000)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='parent'
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.blog}'

    class Meta: 
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Like(models.Model):
    '''Модель лайка, чтобы лайкать отзывы под статьей'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)