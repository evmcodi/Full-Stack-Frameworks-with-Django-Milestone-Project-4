from django.db import models


class Term(models.Model):
    # The user that has created the term object.
    # user = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL)

    # The term that the user enters.
    term = models.CharField(max_length=500, null=False, blank=False)

    # The definition that the user enters.
    definition = models.CharField(max_length=4000, null=True, blank=True)

    def __str__(self):
        return self.term
