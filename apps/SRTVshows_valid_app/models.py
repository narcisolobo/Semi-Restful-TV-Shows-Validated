from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) == 0:
            errors['title1'] = 'Show title cannot be blank.'
        if len(postData['title']) < 2:
            errors['title2'] = 'Show title must be at least 2 characters.'
        if len(postData['network']) == 0:
            errors['network1'] = 'Network cannot be blank.'
        if len(postData['network']) < 3:
            errors['network2'] = 'Network must be at least 3 characters.'
        if len(postData['release-date']) == 0:
            errors['release_date'] = 'Release date cannot be blank.'
        if len(postData['description']) == 0:
            errors['description1'] = 'Show description cannot be blank.'
        if len(postData['description']) < 10:
            errors['description2'] = 'Show description must be at least 10 characters.'
        return errors
    
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    objects = ShowManager()