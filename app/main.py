from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(1, "Emma", "Watson")
    Actor.objects.create(2, "Daniel", "Radclife")
    print(Actor.objects.all())

    Actor.objects.update(2, "Daniel", "Radcliffe")
    print(Actor.objects.all())

    Actor.objects.delete(1)
    print(Actor.objects.all())
