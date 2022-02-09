from django.db import models
from django.db.models.signals import m2m_changed, post_save
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
def abstract_m2m_signal(sender, **kwargs):
    wrapped_abstract_m2m(sender, **kwargs)

@receiver(m2m_changed, sender=Concrete.m2m_field.through)
def concrete_m2m_signal(sender, **kwargs):
    wrapped_concrete_m2m(sender, **kwargs)

@receiver(post_save, sender=Abstract)
def abstract_post_save_signal(sender, **kwargs):
    wrapped_abstract_post_save(sender, **kwargs)

def wrapped_abstract_m2m(sender, **kwargs):
    """This function exists to make it easier to mock and count signal calls."""
    pass

def wrapped_concrete_m2m(sender, **kwargs):
    """This function exists to make it easier to mock and count signal calls."""
    pass

def wrapped_abstract_post_save(sender, **kwargs):
    """This function exists to make it easier to mock and count signal calls."""
    pass
