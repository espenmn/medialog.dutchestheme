def get_text(self):
    text = self.data['rich_text']
    return text

def background_image(self):
    bi = self.data['background_image']
    items = self.context.portal_catalog(UID=bi)
    return items[0].getURL()


def get_url(self):
    url = self.data['url']
    if url.startswith('${portal_url}'):
        a, b, c = url.split('/')
        url = '{0}/{1}'.format(b, c)
        context_state = self.context.restrictedTraverse(
            '@@plone_context_state'
        )
        url = '/'.join([
            context_state.canonical_object_url(), url
        ])
    return url
