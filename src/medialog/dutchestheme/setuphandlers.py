# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api
import os
#from plone.app.textfield.value import RichTextValue
from plone.namedfile.file import NamedBlobImage

def post_install(context):
    """add favicons etc"""
    portal = api.portal.get()
    _create_content(portal)

def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.

def _create_content(portal):
    """Lets create the icons and the user can customize them"""
    titles = [
        'favicon.png',
        'apple-touch-icon-57x57-precomposed.png',
        'apple-touch-icon-72x72-precomposed.png',
        'apple-touch-icon-114x114-precomposed.png',
        'apple-touch-icon-144x144-precomposed.png',
        'apple-touch-icon-precomposed.png',
        'apple-touch-icon.png'
        ]

    for i_image in titles:
        if not portal.get(i_image, False):
            icon_image = api.content.create(
                type='Image',
                container=portal,
                id=i_image,
                title=i_image,
            )
            icon_image.image = load_image(i_image)

def load_image(i_image):
    filename = os.path.join(os.path.dirname(__file__), 'theme',
                            '{0}'.format(i_image))
    return NamedBlobImage(
        data=open(filename, 'r').read(),
        filename=u'{0}'.format(i_image)
    )
