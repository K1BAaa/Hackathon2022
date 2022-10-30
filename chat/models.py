from django.db import models
from form.models import VectorInterest #VECTOR


class VectorsChats(models.Model):
    all_vectors = ['sport', 'music', 'art', 'travel', 'book', 'nature', 'learning', 'food', 'computer', 'movie']
    sport = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    music = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    art = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    travel = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    book = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    nature = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    learning = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    food = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    computer = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    movie = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


class SuggestedChats(models.Model):
    all_vectors = VectorsChats().all_vectors
    user_vector = VectorInterest().vector #VECTOR
    user_negative_chat = all_vectors[min(enumerate(user_vector), key=lambda x: x[1])[0]]
    user_two_chats = []

    def define_chats(self):
        max_two_value = [0, max(self.user_vector)]
        max_two_index = [0, max(enumerate(self.user_vector), key=lambda x: x[1])[0]]

        for i in range(len(self.user_vector)):
            if self.user_vector[i] >= max_two_value[0] > max_two_value[1]:
                max_two_index[0] = i
                max_two_value[0] = self.user_vector[i]
        self.user_chats = [self.all_vectors[max_two_index[0]], self.all_vectors[max_two_index[1]]]

