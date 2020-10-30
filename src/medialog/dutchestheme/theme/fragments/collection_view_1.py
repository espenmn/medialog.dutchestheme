def get_items(self):
    linked = self.data['linked_folder'] or self.data['select_folder']
    if linked:
        folder = self.context.portal_catalog(UID=linked)
        return folder[0].getObject()
    return self.context

def ctype(self):
    if 'ctype' in self.data.keys():
        return self.data['ctype']
    return True

def csubject(self):
    if 'csubject' in self.data.keys():
        return self.data['csubject']
    return None

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
