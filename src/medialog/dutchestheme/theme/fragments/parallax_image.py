def one_image(self):
    item =  self.data['background_image']
    items =self.context.portal_catalog(UID=item)
    return items[0]
    