import graphene
from .models import Task
from graphene_django.types import DjangoObjectType

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ("id", "name", "date")


class Query(graphene.ObjectType):
    all_task = graphene.List(TaskType)

    def resolve_all_task(root, info):
        return Task.objects.all()

schema = graphene.Schema(query=Query)