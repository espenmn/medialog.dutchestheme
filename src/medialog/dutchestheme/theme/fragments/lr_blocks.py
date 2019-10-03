def get_items(self):
    linked = self.data['linked_folder']
    folder = self.context.portal_catalog(UID=linked)
    return folder[0].getObject()

def get_item(self):
    linked = self.data['select_folder']
    folder = self.context.portal_catalog(UID=linked)
    return folder[0].getObject()
