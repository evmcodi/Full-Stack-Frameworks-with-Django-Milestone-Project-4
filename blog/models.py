from django.db import models
from django.contrib.auth.models import User




class Blog(models.Model):
    # The user that has created the blog object.
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    # The blog heading that the user enters.
    blog_heading = models.CharField(max_length=500, null=False, blank=False)

    # The blog that the user enters.
    blog = models.TextField(max_length=4000, null=True, blank=True)

    # The creation time of the blog
    created_on = models.DateTimeField(auto_now_add=True, )


    def __str__(self):
        return self.blog_heading

    class Meta:
        # Only allow publishers and admins to add and edit Blog models.
        permissions = [
            ("publish_blog_posts", "Publisher user - can publish, edit and delete blog posts."),
        ]

        # Sort the blogs with the latest first.
        ordering = ['created_on']

