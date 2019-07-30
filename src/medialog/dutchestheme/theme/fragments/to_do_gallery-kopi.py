def get_images(self):
    imagelist = self.data['imagelist']
    image_items = self.context.portal_catalog(UID=imagelist)
    return image_items
