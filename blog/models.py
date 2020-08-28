from django.db import models
from django.contrib.auth.models import User




class Blog(models.Model):
    # The user that has created the blog object.
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    # The blog heading that the user enters.
    blog_heading = models.CharField(max_length=500, null=False, blank=False)

    # The blog that the user enters.
    blog = models.TextField(max_length=4000, null=True, blank=True)


    def __str__(self):
        return self.blog_heading

    class Meta:
        permissions = [
            ("publish_blog_posts", "Publisher user - can publish, edit and delete blog posts."),
        ]

