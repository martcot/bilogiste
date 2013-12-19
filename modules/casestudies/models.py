# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField

class CaseStudy(models.Model):
    name = models.CharField(max_length=255, verbose_name=_(u"Nom du cas d'étude"))
    slug = AutoSlugField(populate_from='name', unique=True)
    photo = models.ImageField(upload_to = "casestudies", verbose_name=_(u"Photo"))
    desc = models.TextField(verbose_name=_(u"Courte description"))
    content = RichTextField(verbose_name=_(u"Contenu"))
    testimony = RichTextField(verbose_name=_(u"Témoignage"), blank=True, null=True)
    pub_date = models.DateTimeField(verbose_name=_("Date de publication"),auto_now=True)
    
    def get_absolute_url(self):
        return reverse('casestudies.views.details', args=[self.slug])

    @property
    def description(self):
        return self.desc
    
    def clean(self, *args, **kwargs):
        from app.ckeditor_cleaner import clean_html
        self.content = clean_html(self.content)
        self.testimony = clean_html(self.testimony)
        
        super(CaseStudy, self).clean(*args, **kwargs)

    def full_clean(self, *args, **kwargs):
        return self.clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(CaseStudy, self).save(*args, **kwargs)
    
    def __str__(self):
        return "%s" % (self.name)
    def __unicode__(self):
        return u'%s' % (self.name)
    
    class Meta:
        app_label = "etudes"
        db_table = "casestudies_case"
        verbose_name = _(u"Étude de cas")
        verbose_name_plural = _(u"Études de cas")
        