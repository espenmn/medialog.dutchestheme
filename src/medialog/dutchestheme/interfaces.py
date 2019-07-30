# -*- coding: utf-8 -*-
from medialog.iconpicker.widgets.widget import ColorPickerFieldWidget
from medialog.controlpanel.interfaces import \
    IMedialogControlpanelSettingsProvider
from plone.supermodel import model
from plone.autoform.directives import widget
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import alsoProvides
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.portlets.interfaces import IColumn
from plone.namedfile.field import NamedBlobImage

_ = MessageFactory('medialog.dutchestheme')


class IMedialogDutchesthemeLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IBelow(IColumn):
    """here we put the below content portlets
    """

class IAbove(IColumn):
    """here we put the above content portlets
    """

class IMedialogDutchesThemeSettings(model.Schema):
    """Adds settings to medialog.controlpanel"""

    model.fieldset(
        'Dutchestheme',
        label=_(u'Dutchestheme'),
        fields=[
            'style',
            'rules',
            'load_css',
            'color1',
            'color2',
            'color3',
            'extra_css']
    )

    style = schema.Choice(
        title=_(u'Style'),
        values=['blue', 'dutchesblue', 'ploneconf', 'red', 'rood', 'scheme1', 'greyish', 'orange', 'paragraf'],
        required=False,
    )

    rules = schema.Choice(
        title=_(u'Layout Rules'),
        values=['default', 'spot', 'spot_2', 'head', 'fullmenu_l'],
        required=True,
    )

    load_css = schema.Bool(
        title=_(u'Load CSS? Put it in your theme and disable it here'),
        required=False,
        default=True,
    )

    color1 = schema.TextLine(
        title=_('color1', default=u'Custom Color 1'),
        required=True,
        description=_('help_color',
                      default='Choose Color'),
    )

    color2 = schema.TextLine(
        title=_('color2', default=u'Custom Color 2'),
        required=True,
        description=_('help_color',
                      default='Choose Color'),
    )

    color3 = schema.TextLine(
        title=_('color3', default=u'Custom Color 3'),
        required=True,
        description=_('help_color',
                      default='Choose Color'),
    )

    extra_css = schema.Text(
        title=_('extra_css', default=u'Extra CSS'),
        required=False,
        description=_('help_extra_css'),
    )

    widget(
        color1=ColorPickerFieldWidget,
        color2=ColorPickerFieldWidget,
        color3=ColorPickerFieldWidget,
    )

alsoProvides(IMedialogDutchesThemeSettings, IMedialogControlpanelSettingsProvider)
