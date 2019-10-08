def item_url(self):
    item =  self.data['link']
    items =self.context.portal_catalog(UID=item)
    return items[0].getURL()

def get_url(self):
    url = self.data['select']
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

def family_css(self):
    #return css_family_class, like fa, wi
    iconset = self.iconset()
    if iconset == 'glyphicon':
         return 'glyphicon'
    if iconset == 'mapicon':
        return 'map-icons'
    if iconset == 'typicon':
        return 'typcn'
    if iconset == 'ionicon':
        return 'ionicons'
    if iconset == 'weathericon':
        return 'wi'
    if iconset == 'octicon' :
        return 'octicon'
    if iconset == 'elusiveicon':
        return 'el-icon'
    if iconset == 'medialogfont':
        return 'medialogfont'
    if iconset == 'iconpickerfont':
        return 'iconpickerfont'
    if iconset == 'lineawsome':
        return 'linewsome'

    return 'fa'

def iconset(self):
    """Returns current iconset name This is also used for loading the resources below"""
    return self.context.portal_registry['medialog.iconpicker.interfaces.IIconPickerSettings.iconset']
    