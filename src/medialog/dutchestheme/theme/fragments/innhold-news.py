def get_items(self):
    item_count = self.data['item_c'] 
    content_type =self.data['content_type']
    sort_on = self.data['sort_on']
    sort_order = str(self.data['sort_order'])
    return self.context.portal_catalog(portal_type=content_type, sort_on=sort_on, sort_order=sort_order)[:item_count]
    
def item_width(self):
    items = self.data['item_c']
    return 100/items