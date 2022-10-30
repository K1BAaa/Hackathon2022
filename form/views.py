import json
from http import HTTPStatus
from django.shortcuts import render
from form.models import VectorInterest, QuestionsVectors #VECTOR


def send_questions(request):
    if request.method == "POST":
        received_json = json.loads(request.body)
        new_vector = VectorInterest() #VECTOR
        all_questions_vectors = QuestionsVectors().all_questions_value
        received_json_data = received_json["data"]
        for i in range(len(new_vector.vector)):
            if received_json_data[i] == '0':
                new_vector.add_vector(all_questions_vectors[i])
            else:
                new_vector.remove_vector(all_questions_vectors[i])
        return render(request, status=HTTPStatus.OK)

    return render(request, 'form/questions_for_form.json')

