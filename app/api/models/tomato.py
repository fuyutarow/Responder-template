import uuid
from django.db import models


class Tomato(models.Model):
    id = models.UUIDField(
        db_index=True, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(default='', max_length=140)
