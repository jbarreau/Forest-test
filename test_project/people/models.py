from django.db import models


# I need an abstract model to test it ; so I made an useless one
class Human(models.Model):
    class Meta:
        unique_together = (("first_name", "last_name"))
        abstract = True

    birth_date = models.DateField(max_length=20)

class Person(Human):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Artist(models.Model):
    WORK_CHOICES = (
        ("guitarist", "guitarist"),
        ("drummer", "drummer"),
        ("singer", "singer"),
        # ...
    )

    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="artist")
    work = models.CharField(max_length=20, choices=WORK_CHOICES)

    def __str__(self) -> str:
        return f"{self.work} : {self.person}"