def image1(self):
    item =  self.data['image1']
    items = self.context.portal_catalog(UID=item)
    return items[0] 
    
def image2(self):
    item =   self.data['image2']
    items =self.context.portal_catalog(UID=item)
    return items[0] 