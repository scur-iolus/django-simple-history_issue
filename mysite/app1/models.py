from django.db import models

from simple_history.models import HistoricalRecords


class Foo(models.Model):
    ...


class Bar(models.Model):
    foo = models.ForeignKey(
        Foo,
        on_delete=models.CASCADE,
        related_name="bars",
        # related_query_name="%(class)s",  # probably better
        related_query_name="bar",  # raises no error
    )
    history = HistoricalRecords()
