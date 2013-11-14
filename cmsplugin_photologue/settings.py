# Default settings of cmsplugin_photologue
# Copy the options You want to customize to Your settings.py

from django.utils.translation import ugettext_lazy as _

# Use CMSPLUGIN_PHOTOLOGUE_PHOTO_TEMPLATES to define list of templates
# available for rendering photologue photos.
# Each template is defined by "id" and "name" pair.
# The template filename is cmsplugin_photologue/photo-{id}.html
CMSPLUGIN_PHOTOLOGUE_PHOTO_TEMPLATES = (
    ('default', _('Default')),
    ('center',  _('Center')),
    ('left',    _('Left')),
    ('right',   _('Right')),
)

# Use CMSPLUGIN_PHOTOLOGUE_GALLERY_TEMPLATES to define list of templates
# available for rendering photologue fotogaleries.
# Each template is defined by "id" and "name" pair.
# The template filename is cmsplugin_photologue/gallery-{id}.html
CMSPLUGIN_PHOTOLOGUE_GALLERY_TEMPLATES = (
    ('default', _('Default')),
)

