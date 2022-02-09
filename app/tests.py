from unittest.mock import patch
from django.test import TestCase
from app.models import Concrete, Other, OtherRelated

def mock_signal(sender, **kwargs):
    pass

class MyTest(TestCase):

    @patch('app.models.wrapped_abstract_m2m', side_effect=mock_signal)
    def test_abstract_m2m_signal_not_called(self, signal_mock):
        other = Other.objects.create()
        related = OtherRelated.objects.create()
        other.m2m_field.add(related)
        self.assertEqual(signal_mock.call_count, 0)

    @patch('app.models.wrapped_concrete_m2m', side_effect=mock_signal)
    def test_concrete_m2m_signal_not_called(self, signal_mock):
        other = Other.objects.create()
        related = OtherRelated.objects.create()
        other.m2m_field.add(related)
        self.assertEqual(signal_mock.call_count, 0)

    @patch('app.models.wrapped_abstract_post_save', side_effect=mock_signal)
    def test_abstract_post_save_not_called(self, signal_mock):
        other = Other()
        other.save()
        self.assertEqual(signal_mock.call_count, 0)

    @patch('app.models.wrapped_abstract_post_save', side_effect=mock_signal)
    def test_abstract_post_save_called(self, signal_mock):
        concrete = Concrete()
        concrete.save()
        self.assertNotEqual(signal_mock.call_count, 0)
