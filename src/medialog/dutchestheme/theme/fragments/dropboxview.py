def get_items(self):
    linked = self.data['linked_folder'] or self.data['select_folder']
    folder = self.context.portal_catalog(UID=linked)
    return folder[0].getObject()

def get_margin(self):
    image_width = self.data['image_width']
    return image_width /20

def get_width(self):
    image_width = self.data['image_width']
    max_images = self.data['max_images']
    return image_width * 1.10 * max_images
