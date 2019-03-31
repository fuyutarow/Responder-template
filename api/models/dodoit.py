import uuid
from django.db import models


class Dodoit(models.Model):
    id = models.UUIDField(
        db_index=True, primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(default='', max_length=140)
