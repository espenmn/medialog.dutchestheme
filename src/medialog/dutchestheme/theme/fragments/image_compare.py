def image1(self):
    item =  self.data['image1'] or self.data['image1b'] 
    items = self.context.portal_catalog(UID=item)
    return items[0].getObject()
    
def image2(self):
    item =   self.data['image2'] or self.data['image2b'] 
    items =self.context.portal_catalog(UID=item)
    return items[0].getObject()
