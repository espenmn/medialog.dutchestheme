def get_item(self):
    item =  self.data['link'].encode('ascii')
    items =self.context.portal_catalog(UID=item)
    return items[0]


def item_url(self):
    item =  self.data['link']
    items =self.context.portal_catalog(UID=item)
    return items[0].getURL()
