# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from medialog.dutchestheme.testing import MEDIALOG_DUTCHESTHEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that medialog.dutchestheme is properly installed."""

    layer = MEDIALOG_DUTCHESTHEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if medialog.dutchestheme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'medialog.dutchestheme'))

    def test_browserlayer(self):
        """Test that IMedialogDutchesthemeLayer is registered."""
        from medialog.dutchestheme.interfaces import (
            IMedialogDutchesthemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IMedialogDutchesthemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MEDIALOG_DUTCHESTHEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['medialog.dutchestheme'])

    def test_product_uninstalled(self):
        """Test if medialog.dutchestheme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'medialog.dutchestheme'))

    def test_browserlayer_removed(self):
        """Test that IMedialogDutchesthemeLayer is removed."""
        from medialog.dutchestheme.interfaces import \
            IMedialogDutchesthemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMedialogDutchesthemeLayer, utils.registered_layers())
