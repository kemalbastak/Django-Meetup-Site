from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    email = models.EmailField(unique=True, max_length=254)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField(max_length=254)
    date = models.DateField()
    slug = models.SlugField(null=True, unique=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null=True)

    def __str__(self) -> str:
        # we do this because in admin page this will show up otherwise we would see the 'Meetup object()'
        return f'{self.title} - {self.slug}'
