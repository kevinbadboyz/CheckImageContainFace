from django.db import models

class Category(models.Model):
    category = models.CharField(max_length = 200)

    def __str__(self):
        return self.category

class Profile(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    avatar = models.ImageField()

    def __str__(self):
        return self.category.category