# -*- coding: utf-8 -*-
from datetime import date
from plone.app.layout.viewlets import ViewletBase
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from plone.app.layout.viewlets.common import ViewletBase
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import ISiteSchema
from Products.CMFPlone.utils import getSiteLogo
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from zope.component import getUtility
from plone import api
from medialog.dutchestheme.interfaces import IMedialogDutchesThemeSettings

class JSHeadViewlet(ViewletBase):
    """ A viewlet which renders the js."""
    
    def render(self):
        js_head =  api.portal.get_registry_record('medialog.dutchestheme.interfaces.IMedialogDutchesThemeSettings.jshead')
        if js_head:
            return js_head
        return "<script></script>"
    
class JSFooterViewlet(ViewletBase):
    """ A viewlet which renders the js."""
    
    # def __init__(self, context):
    #     js_footer =  api.portal.get_registry_record('medialog.dutchestheme.interfaces.IMedialogDutchesThemeSettings.jsfooter')
        
    
    def render(self):
        js_footer =  api.portal.get_registry_record('medialog.dutchestheme.interfaces.IMedialogDutchesThemeSettings.jsfooter')
        if js_footer:
            return js_footer
        return "<script></script>"


class MenuViewlet(GlobalSectionsViewlet):
    """ A viewlet which renders the menu."""

    @property
    def logo_title(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ISiteSchema,
                                     prefix="plone",
                                     check=False)
        return settings.site_title

    @property
    def img_src(self):
        return  getSiteLogo()


class BelowViewlet(ViewletBase):
    index = ViewPageTemplateFile('belowportlets.pt')

    def update(self):
        super(BelowViewlet, self).update()
        self.year = date.today().year

    def render_below_portlets(self):
        """

        """
        portlet_manager = getMultiAdapter(
            (self.context, self.request, self.__parent__), name='medialog.dutchestheme.belowportlets')
        portlet_manager.update()
        return portlet_manager.render()


class AboveViewlet(ViewletBase):
    index = ViewPageTemplateFile('aboveportlets.pt')

    def update(self):
        super(AboveViewlet, self).update()
        self.year = date.today().year

    def render_above_portlets(self):
        """

        """
        portlet_manager = getMultiAdapter(
            (self.context, self.request, self.__parent__), name='medialog.dutchestheme.aboveportlets')
        portlet_manager.update()
        return portlet_manager.render()


#class AboveAllViewlet(AboveViewlet):
#    index = ViewPageTemplateFile('aboveallportlets.pt')



class AboveFooterViewlet(AboveViewlet):
    index = ViewPageTemplateFile('abovefooterportlets.pt')
