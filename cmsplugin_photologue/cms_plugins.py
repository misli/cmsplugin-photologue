from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from photologue.models import Photo, Gallery
from cmsplugin_photologue.models import PhotologuePhoto, PhotologueGallery

from django.conf import settings
from django.utils.translation import ugettext as _


class PhotologuePhotoPlugin(CMSPluginBase):
    model = PhotologuePhoto
    name = _('Photologue Photo')
    text_enabled = True
    fields = ('obj', 'template', 'display_size', 'link_size', 'display_link')

    def render(self, context, instance, placeholder):
        context.update({
            'plugin': instance,
            'photo': instance.photo,
            'placeholder': placeholder,
        })
        return context

    def get_render_template(self, context, instance, placeholder):
        return 'cmsplugin_photologue/photo-{}.html'.format(instance.template)

    def icon_src(self, instance):
        return instance.photo.plugin_display_url


class PhotologueGalleryPlugin(CMSPluginBase):
    model = PhotologueGallery
    name = _('Photologue Gallery')
    fields = ('obj', 'template', 'display_size', 'link_size', 'display_link', 'order', 'limit')

    def render(self, context, instance, placeholder):
        context.update({
            'plugin': instance,
            'gallery': instance.gallery,
            'placeholder': placeholder,
        })
        return context

    def get_render_template(self, context, instance, placeholder):
        return 'cmsplugin_photologue/gallery-{}.html'.format(instance.template)


plugin_pool.register_plugin(PhotologueGalleryPlugin)
plugin_pool.register_plugin(PhotologuePhotoPlugin)

