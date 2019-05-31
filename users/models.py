from django.db import models


class User(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    last_name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(null=False, unique=True)
    username = models.CharField(null=False, blank=False, max_length=100,  unique=True)
    birthdate = models.DateField(null=False)

    def __repr__(self):
        return '{username}: {name} {last_name} - {email}'.format(
            username=self.username,
            name=self.name,
            last_name=self.last_name,
            email=self.email,
        )

    def __str__(self):
        return '{username}: {name} {last_name} - {email}'.format(
            username=self.username,
            name=self.name,
            last_name=self.last_name,
            email=self.email,
        )
