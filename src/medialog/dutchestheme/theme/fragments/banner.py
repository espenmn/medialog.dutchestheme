def get_theurl(self):
    link =  self.data['link']
    if link:
        item =  link.encode('ascii','ignore')
        items =self.context.portal_catalog(UID=item)
        irurl = items[0].getURL()
        return irurl.encode('ascii','ignore')

    url = self.data['select']

    if url:
        if url.startswith('${portal_url}'):
            spl_url =  (url.split('/'))[1:]
            url = '/'.join(spl_url)
            context_state = self.context.restrictedTraverse(
                '@@plone_context_state'
            )
            url = '/'.join([
                context_state.canonical_object_url(), url
            ])
        return url

    return '#'
