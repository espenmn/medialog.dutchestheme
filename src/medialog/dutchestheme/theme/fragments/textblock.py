def item(self):
    item = load_item(self)
    return item

def item_url(self):
    item = load_item(self)
    return item.getURL()

def load_item(self):
    item =  self.data['image1']
    items =self.context.portal_catalog(UID=item)
    return items[0]
