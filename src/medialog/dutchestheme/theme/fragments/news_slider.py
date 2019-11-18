def get_items(self):
    limit = self.data['limit']
    subjects = self.data['subjects']
    language = self.context.Language()

    if subjects:
            return self.context.portal_catalog(portal_type='News Item', Language=language, Subject=subjects, sort_on='modified', sort_order='descending')[:limit]

    return self.context.portal_catalog(portal_type='News Item', Language=language, sort_on='modified', sort_order='descending')[:limit]
