from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


class Writer(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=20, null=True, blank=True)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=30, null=True, blank=True)
    sure_name = models.CharField(verbose_name=_('Sure Name'), max_length=20, null=True, blank=True)
    creation_date = models.DateTimeField(default=now, editable=False, verbose_name=_('Creation date'))

    def __str__(self):
        return '{first_name} {last_name} ({sure_name})'.format(first_name=self.first_name, last_name=self.last_name,
                                                               sure_name=self.sure_name)


class Publisher(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('Name'), max_length=20)
    phone = models.CharField(max_length=11, verbose_name=_('PhoneNumber'), null=True,
                             blank=True)  # Use char field for example 021111111
    address = models.TextField(blank=True, null=True, verbose_name=_('Address'))
    creation_date = models.DateTimeField(default=now, editable=False, verbose_name=_('Creation date'))

    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    pages = models.IntegerField(verbose_name=_('Number of pages'), default=0, validators=[MinValueValidator(0)])
    publish_year = models.IntegerField(verbose_name=_('Publish year'))
    writers = models.ManyToManyField(Writer, verbose_name=_('Writers'))
    publisher = models.ForeignKey(Publisher, verbose_name=_('Publisher'), on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=now, editable=False, verbose_name=_('Creation date'))

    def __str__(self):
        return self.title
