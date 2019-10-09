def get_url(self):
    url = self.data['url']
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
