from zope.interface import directlyProvides
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from plone import api

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.dutchestheme')


def ShowImagesVocabulary(context):

    images = api.content.find(portal_type='Image')

    if images:
        terms = [ SimpleTerm(value=img.UID, token=img.UID, title=img.Title) for img in images ]

    return SimpleVocabulary(terms)

directlyProvides(ShowImagesVocabulary, IVocabularyFactory)
