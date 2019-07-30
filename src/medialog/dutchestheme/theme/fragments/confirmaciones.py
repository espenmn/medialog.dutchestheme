def get_items(self):
    return self.context.portal_catalog(portal_type='movie')
