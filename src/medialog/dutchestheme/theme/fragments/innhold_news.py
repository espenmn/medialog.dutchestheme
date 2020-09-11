def get_items(self):
    item_count = self.data['item_c']
    content_type = self.data['content_type']
    sort_on = self.data['sort_on']
    sort_order = str(self.data['sort_order'])
    language = self.context.Language()

    keyword = self.get_keyword()
    if keyword:
        return  self.context.portal_catalog(portal_type=content_type, Language=language, Subject=keyword, sort_on=sort_on, sort_order=sort_order)[:item_count]

    return self.context.portal_catalog(portal_type=content_type, Language=language, sort_on=sort_on, sort_order=sort_order)[:item_count]


def item_width(self):
    items = self.data['item_r']
    return 100/items

def get_keyword(self):
    keyord = self.data['keyword']
    return [s.encode('ascii', 'ignore') for s in keyord]
