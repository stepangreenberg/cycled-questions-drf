from rest_framework import serializers
from .models import Creature, Question


class CreatureQuestionForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        if "pk" in self.context["view"].kwargs:
            return Question.objects.filter(
                creature__name=self.context["view"].kwargs["pk"]
            )

        return Question.objects.none()


class CreatureCreateSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="question-detail",
        read_only=True,
    )

    class Meta:
        model = Creature
        fields = ("url", "name", "questions", "current_question")


class CreatureRUDSerializer(serializers.HyperlinkedModelSerializer):
    current_question = CreatureQuestionForeignKey()
    questions = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="question-detail",
        read_only=True,
    )

    class Meta:
        model = Creature
        fields = ("url", "name", "questions", "current_question")


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ("url", "id", "text", "creature")
