from django.db import models
from django.utils.html import format_html

# Create Category models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:30px;height:30px;border-radius:50%;" />'.format(self.image))

    def __str__(self):
        return self.title

    class Meta:
        db_table = "categories"


# Create Post models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    url = models.CharField(max_length=255)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='categories/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:30px;height:30px;border-radius:50%;" />'.format(self.image))

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"
