from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

from .models import Creature, Question
from .serializers import (
    QuestionSerializer,
    CreatureRUDSerializer,
    CreatureCreateSerializer,
)


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "yield_question": reverse(
                "yield_question",
                kwargs={"name": "test"},
                request=request,
                format=format,
            ),
            "cycled_questions": [
                reverse("creature-list", request=request, format=format),
                reverse("question-list", request=request, format=format),
            ],
            "swagger": reverse("schema-swagger-ui", request=request, format=format),
        }
    )


@api_view(["GET"])
def yield_question(request, name, format=None):
    creature = Creature.objects.get(name=name)
    questions = list(creature.questions.all())
    selected_question = creature.current_question
    selected_question_index = questions.index(selected_question)

    next_question = (
        questions[selected_question_index + 1]
        if selected_question_index != len(questions) - 1
        else questions[0]
    )

    creature.current_question = next_question
    creature.save()

    serializer_class = QuestionSerializer(
        selected_question, context={"request": request}
    )
    return Response(serializer_class.data)


class CreatureViewSet(ModelViewSet):
    queryset = Creature.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreatureCreateSerializer
        return CreatureRUDSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
