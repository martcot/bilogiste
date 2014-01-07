# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField

class BlogPostCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_(u"Nom de la catégorie"))
    slug = AutoSlugField(populate_from='name', unique=True)
    
    def get_absolute_url(self):
        return reverse('blog.views.index', args=[self.slug])
    
    @property
    def posts(self):
        return BlogPost.objects.filter(category=self, statut="published")
    
    @property
    def lastitem(self):
        try:
            return BlogPost.objects.filter(category=self, statut="published").order_by('-pub_date')[0]
        
        except:
            return None
        
    def __str__(self):
        return "%s" % (self.name)
    def __unicode__(self):
        return u'%s' % (self.name)
    
    class Meta:
        app_label = "blog"
        db_table = "blog_category"
        verbose_name = _(u"Catégorie d'articles")
        verbose_name_plural = _(u"Catégories d'articles")

        
class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Titre"))
    photo = models.ImageField(upload_to = "blog", verbose_name=_(u"Photo"))
    desc = models.TextField(verbose_name=_(u"Description"))
    
    @property
    def posts(self):
        return BlogPost.objects.filter(author=self)
    
    def __str__(self):
        return "%s" % (self.name)
    def __unicode__(self):
        return u'%s' % (self.name)
    
    class Meta:
        app_label = "blog"
        db_table = "blog_author"
        verbose_name = _(u"Auteur d'articles")
        verbose_name_plural = _(u"Auteurs d'articles")

def PostStatut():
    return (
        ("waiting",_(u"En attente")),
        ("corrected",_(u"Corrigé")),
        ("published",_(u"Publié")),
    )

class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Titre de l'article"))
    statut = models.CharField(max_length=25,
                            choices=PostStatut(),
                            default='waiting',
                            verbose_name = _(u"Statut"),)
    slug = AutoSlugField(populate_from='title', unique=True)
    photo = models.ImageField(upload_to = "blog", verbose_name=_(u"Photo"), blank=True, null=True)
    desc = models.TextField(verbose_name=_(u"Courte description"))
    content = RichTextField(verbose_name=_(u"Contenu"))
    pub_date = models.DateTimeField(verbose_name=_("Date de publication"),auto_now=True)
    category = models.ForeignKey(BlogPostCategory, verbose_name=_(u"Catégorie"))
    author = models.ForeignKey(Author, verbose_name=_(u"Auteur"))
    
    def get_absolute_url(self):
        return reverse('blog.views.details', args=[self.category.slug,self.slug])

    @property
    def description(self):
        return self.desc
    
    def clean(self, *args, **kwargs):
        from app.ckeditor_cleaner import clean_html
        self.content = clean_html(self.content)
        
        super(BlogPost, self).clean(*args, **kwargs)

    def full_clean(self, *args, **kwargs):
        return self.clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(BlogPost, self).save(*args, **kwargs)
    
    def __str__(self):
        return "%s" % (self.title)
    def __unicode__(self):
        return u'%s' % (self.title)
    
    class Meta:
        app_label = "blog"
        db_table = "blog_post"
        verbose_name = _(u"Article")
        verbose_name_plural = _(u"Articles")
        