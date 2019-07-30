def css_class(self):
    card_items = int(self.data['card_items'])
    return (12/card_items)

def get_items(self):
 card_items = int(self.data['card_items'])
 keyword = self.data['keyword']
 return self.context.portal_catalog(sort_on='modified', sort_order='ascending', Subject=keyword)[:card_items];
