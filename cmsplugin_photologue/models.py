from django.db import models
from django.conf import settings
from .settings import *
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from cms.models import CMSPlugin
from photologue.models import Gallery, Photo, PhotoSize

import random


PHOTO_TEMPLATES   = getattr(settings, 'CMSPLUGIN_PHOTOLOGUE_PHOTO_TEMPLATES',
                                       CMSPLUGIN_PHOTOLOGUE_PHOTO_TEMPLATES)

GALLERY_TEMPLATES = getattr(settings, 'CMSPLUGIN_PHOTOLOGUE_GALLERY_TEMPLATES',
                                       CMSPLUGIN_PHOTOLOGUE_GALLERY_TEMPLATES)

ORDER_CHOICES = (
    ('gallery', _('Gallery Order')),
    ('latest',  _('Latest first')),
    ('oldest',  _('Oldest first')),
    ('random',  _('Random order')),
)


class PhotologuePlugin(CMSPlugin):
    display_size = models.ForeignKey(PhotoSize, verbose_name=_('Display size'), related_name='+', blank=True, null=True)
    link_size    = models.ForeignKey(PhotoSize, verbose_name=_('Link size'),    related_name='+', blank=True, null=True)
    display_link = models.BooleanField(_('Display link'), default=False)

    def _add_size_attributes(self, photo):
        if self.display_size:
            setattr(photo, 'plugin_display_url',  photo._get_SIZE_url(size=self.display_size.name))
            setattr(photo, 'plugin_display_size', photo._get_SIZE_size(size=self.display_size.name))
        else:
            setattr(photo, 'plugin_display_url',  photo.image.url)
            setattr(photo, 'plugin_display_size', (photo.image.width, photo.image.height))
        if self.link_size:
            setattr(photo, 'plugin_link_url',  photo._get_SIZE_url(size=self.link_size.name))
            setattr(photo, 'plugin_link_size', photo._get_SIZE_size(size=self.link_size.name))
        else:
            setattr(photo, 'plugin_link_url',  photo.image.url)
            setattr(photo, 'plugin_link_size', (photo.image.width, photo.image.height))
        return photo

    def copy_relations(self, oldinstance):
        self.obj          = oldinstance.obj
        self.display_size = oldinstance.display_size
        self.link_size    = oldinstance.link_size

    def __unicode__(self):
        return unicode(self.title)

    @property
    def title(self):
        if self.obj:
            return self.obj.title
        else:
            return _('all')
        

    @property
    def title_slug(self):
        if self.obj:
            return self.obj.title_slug
        else:
            return 'all'

    class Meta:
        abstract = True



class PhotologuePhoto(PhotologuePlugin):
    obj = models.ForeignKey(Photo, verbose_name=_('photo'))
    template     = models.CharField(_('template'), max_length=100, choices=PHOTO_TEMPLATES,
                                default=PHOTO_TEMPLATES[0][0],
                                help_text=_('The template used to render the image.'))

    @property
    def render_template(self):
        return 'cmsplugin_photologue/photo-%s.html' % self.template

    @property
    def photo(self):
        return self._add_size_attributes(self.obj)


class PhotologueGallery(PhotologuePlugin):
    obj = models.ForeignKey(Gallery, verbose_name=_('gallery'), blank=True, null=True)
    order = models.CharField(_('order'), max_length=8, default='gallery', choices=ORDER_CHOICES)
    limit = models.PositiveIntegerField(default=0, help_text=u'0 means no limit')
    template = models.CharField(_("template"), max_length=100, choices=GALLERY_TEMPLATES,
                                default=GALLERY_TEMPLATES[0][0],
                                help_text=_('The template used to render the gallery.'))

    @property
    def render_template(self):
        return 'cmsplugin_photologue/gallery-%s.html' % self.template

    @property
    def gallery(self):
        return self.obj

    @property
    def photos(self):
        if self.obj:
            photo_set = self.obj.photos
        else:
            photo_set = Photo.objects
        photo_set = photo_set.filter(is_public=True)
        if self.order == 'latest':
            photo_set = photo_set.order_by('-date_added', '-id')
        elif self.order == 'oldest':
            photo_set = photo_set.order_by('date_added', 'id')
        if self.limit:
            photos = list(photo_set[:self.limit])
        else:
            photos = list(photo_set)
        if self.order == 'random':
            random.shuffle(photos)
        return map(self._add_size_attributes, photos)

    def get_breadcrumb(self):
        breadcrumb = super(PhotologueGallery, self).get_breadcrumb()
        if self.obj:
            breadcrumb.append({'url': reverse('admin:photologue_gallery_change', args=[self.obj.id]), 'title': unicode(self.obj)})
        return breadcrumb

