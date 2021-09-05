from django.contrib.auth.models import Group

group = Group(name="Clientes")
group.save()

group = Group(name="Gestores")
group.save()