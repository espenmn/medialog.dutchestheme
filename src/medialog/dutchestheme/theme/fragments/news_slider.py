def get_items(self):
    limit = self.data['limit']
    subjects = self.data['subjects']
    if subjects:
            return self.context.portal_catalog(portal_type='News Item', Subject=subjects, sort_on='modified', sort_order='descending')[:limit]

    return self.context.portal_catalog(portal_type='News Item', sort_on='modified', sort_order='descending')[:limit]
