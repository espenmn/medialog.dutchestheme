def get_items(self):
    item_count = self.data['item_c']
    language = self.context.Language()
    linked = self.data['linked_folder']
    folder_path = '/'.join(context.getPhysicalPath())

    if linked:
        folder_path = self.get_path()

    return self.context.portal_catalog(portal_type='Event', path={'query': folder_path,}, Language=language, sort_on='start')[:item_count]

def get_path(self):
    linked = self.data['linked_folder']
    folder = self.context.portal_catalog(UID=linked)
    mappe =  folder[0].getObject()
    return  '/'.join(mappe.getPhysicalPath())
