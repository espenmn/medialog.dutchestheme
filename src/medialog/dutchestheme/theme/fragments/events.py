def get_items(self):
    item_count = self.data['item_c']
    language = self.context.Language()
    keyword = self.get_keyword()
    from DateTime import DateTime
    date_range = {
        'query': (
            DateTime(),
        ),
        'range': 'min',
    }

    if keyword:
        return  self.context.portal_catalog(portal_type='Event', end=date_range, Language=language, Subject=keyword, sort_on='start')[:item_count]

    return self.context.portal_catalog(portal_type='Event', end=date_range, Language=language, sort_on='start')[:item_count]

def get_keyword(self):
    keyord = self.data['keyword']
    return [s.encode('ascii', 'ignore') for s in keyord]
