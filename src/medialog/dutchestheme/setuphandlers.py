# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api
import os
from plone.app.textfield.value import RichTextValue

def post_install(context):
    """add front-page script"""
    #Add front page
    #portal = api.portal.get()
    #_create_frontpage(portal)

def install_demo_content(context):
    """add content script"""
    #Add demo content
    #portal = api.portal.get()
    #_create_content(portal)

def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
