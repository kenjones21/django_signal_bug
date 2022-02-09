from unittest.mock import patch
from django.test import TestCase
from app.models import Other, OtherRelated

def mock_signal(sender, **kwargs):
    print(sender)
    print('mocked')

class MyTest(TestCase):

    @patch('app.models.wrapped_function', side_effect=mock_signal)
    def test_example(self, signal_mock):
        other = Other.objects.create()
        related = OtherRelated.objects.create()
        other.m2m_field.add(related)
        self.assertEqual(signal_mock.call_count, 0)
