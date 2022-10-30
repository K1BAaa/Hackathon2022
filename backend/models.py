from django.db import models
from social_django.models import (
    AbstractUserSocialAuth
)


class VectorInterest(models.Model):
    sport = 0
    music = 0
    art = 0
    travel = 0
    book = 0
    nature = 0
    learning = 0
    food = 0
    computer = 0
    movie = 0
    vector = [sport, music, art, travel, book, nature, learning, food, computer, movie]

    def add_vector(self, vector):
        for i in range(len(self.vector)):
            self.vector[i] += vector[i]

    def remove_vector(self, vector):
        for i in range(len(self.vector)):
            self.vector[i] -= vector[i]

    def update_on_null_vector(self):
        self.vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def update_vector(self, vector):
        self.vector = vector


class User(AbstractUserSocialAuth):
    vector = models.OneToOneField(
            VectorInterest, on_delete=models.CASCADE,
    )
