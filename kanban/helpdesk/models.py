from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'statuses'

    def __str__(self):
        return self.name


class Engineer(models.Model):
    name = models.CharField(max_length=100)
    # Image filename is the name of an image file in the helpdesk/img directory.
    image_filename = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_image_url(self):
        return f'helpdesk/img/{self.image_filename}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=100)
    sort_order = models.IntegerField()
    color = models.CharField(max_length=8)

    class Meta:
        verbose_name_plural = 'priorities'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(Engineer, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    rank = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
