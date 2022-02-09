from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class Related(models.Model):
    pass

class Abstract(models.Model):
    m2m_field = models.ManyToManyField(to=Related)
    int_field = models.IntegerField(default=0)
    class Meta:
        abstract = True

class Concrete(Abstract):
    pass

class OtherRelated(models.Model):
    pass

class Other(models.Model):
    m2m_field = models.ManyToManyField(to=OtherRelated)

@receiver(m2m_changed, sender=Abstract.m2m_field.through)
def abstract_signal(sender, **kwargs):
    wrapped_function(sender, **kwargs)

@receiver(m2m_changed, sender=Concrete.m2m_field.through)
def concrete_signal(sender, **kwargs):
    wrapped_function(sender, **kwargs)

def wrapped_function(sender, **kwargs):
    pass
