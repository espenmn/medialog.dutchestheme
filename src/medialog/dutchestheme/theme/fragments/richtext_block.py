def get_text(self):
    text = self.data['rich_text']
    return text

def background_image(self):
    bi = self.data['background_image']
    items = self.context.portal_catalog(UID=bi)
    return items[0].getURL()
    
