from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=30)
    level = models.CharField(max_length=3)

    class Meta:
        ordering = ['id']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class Category(models.Model):
    engname = models.CharField(max_length=25)
    rusname = models.CharField(max_length=25)
 
    class Meta:
        ordering = ['id']
        verbose_name = 'Work Category'
        verbose_name_plural = 'Work Categories'

    def __str__(self):
        return self.rusname

class Work(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='works')
    image = models.ImageField(upload_to='works')
    description = models.TextField()
    stack = models.TextField()
    link = models.URLField(max_length=200)
 
    class Meta:
        ordering = ['-id']
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=25)
    icon = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']
        verbose_name = 'Acheivement'
        verbose_name_plural = 'Acheivements'

    def __str__(self):
        return self.name    

class Item(models.Model):
    name = models.CharField(max_length=150)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name    



class Author(models.Model):
    name = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    about = models.TextField()
    skills = models.ManyToManyField(Skill, related_name='author')
    image = models.ImageField(upload_to='author')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.name} {self.lastname}'


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'Message from {self.name}: {self.subject}'   

class Testimony(models.Model):
    name = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)  
    image = models.ImageField(upload_to='clients') 
    text = models.TextField()     

    class Meta:
        ordering = ['-id']
        verbose_name = 'Recommendation'
        verbose_name_plural = 'Recommendations'

    def __str__(self):
        return f'{self.name} {self.lastname}'