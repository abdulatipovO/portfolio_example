from tabnanny import verbose
from django.db import models

# Create your models here.


class CategoryBlog(models.Model):
    title = models.CharField(max_length=55)
     
    class Meta:
        verbose_name = "Blog Kategoriya"
        verbose_name_plural= "Blog Kategoriyalar"

    def __str__(self) -> str:
        return self.title


class CategoryWork(models.Model):
    title = models.CharField(max_length=55)
     
    class Meta:
        verbose_name = "Ish Kategoriya"
        verbose_name_plural= "Ish Kategoriyalar"

    def __str__(self) -> str:
        return self.title
    

class BlogPost(models.Model):
    category_blog = models.ForeignKey(CategoryBlog,on_delete=models.PROTECT)
    title = models.CharField(max_length=55)
    text = models.TextField()
    images = models.ImageField(upload_to='images')
    reg_date = models.DateField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.title

class MyWork(models.Model):
    category_work = models.ForeignKey(CategoryWork,on_delete=models.PROTECT)
    project_name = models.CharField(max_length=55)
    images = models.ImageField(upload_to="work_images")
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.project_name


class ContactForm(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    subject = models.CharField(max_length=55)
    text = models.TextField()
    reg_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name


class Subcribe(models.Model):
    email = models.EmailField()
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email
