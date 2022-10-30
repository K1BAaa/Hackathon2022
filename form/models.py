from django.db import models


class QuestionsVectors(models.Model):
    all_questions_value = [
        [0.1, 0, 0, 0.3, 0, 0.6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0.1, 0, 0.8, 0.1],
        [0, 0.8, 0, 0, 0, 0, 0, 0, 0, 0.2],
        [0.9, 0, 0, 0, -0.2, 0.3, 0, 0, 0, 0],
        [0.2, 0, 0, 0.3, 0, 0.9, 0, 0, -0.4, 0],
        [0, 0, 0.9, 0, 0, 0.1, 0, 0, 0, 0],
        [0, 0.3, 0.1, 0, -0.3, 0, 0, 0, 0, 0.9],
        [0, 0, 0.1, 0, 0, 0.9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0.8, 0, 0, 0.2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0.8, 0, 0, 0.8, 0],
        [0.3, 0, 0, 0.6, 0, 0.1, 0, 0, 0, 0],
        [-0.2, 0, 0, 0, 0, 0, 0, 0, 0.2, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0.8, 0, 0, 0, 0, 0.2, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    ]


class VectorInterest:
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
