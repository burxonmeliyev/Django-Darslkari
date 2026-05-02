from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    file = models.FileField(upload_to='news_file/', blank=True, null=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    tags = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def tag_list(self):
        if not self.tags:
            return []
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_comments')
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.content[:50]}"

    class Meta:
        ordering = ['-created_at']
