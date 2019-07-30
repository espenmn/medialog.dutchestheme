def get_items(self):
    linked = self.data['linked_folder']
    folder = self.context.portal_catalog(UID=linked)
    return folder[0].getObject()
    #.getURL()

def ctype(self):
    if 'ctype' in self.data.keys(): 
        return self.data['ctype']
    return True
    
def csubject(self):
    if 'csubject' in self.data.keys(): 
        return self.data['csubject']
    return None
