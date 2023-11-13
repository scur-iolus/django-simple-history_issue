from django.test import TestCase
from app1.models import Foo, Bar


class MyTestClass(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        foo = Foo()
        foo.save()
        _ = Bar(foo_id=foo.id).save()

    def test_reverse_fk(self) -> None:
        self.assertTrue(Foo.objects.filter(bar__isnull=False).count())

    # def test_historical_reverse_fk(self) -> None:
    #     self.assertTrue(Foo.objects.filter(historicalbar__isnull=False).count())
