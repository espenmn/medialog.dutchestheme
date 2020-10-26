def get_wallitems(self):
    linked = self.data['linked_folder'] or self.data['select_folder']
    folder = self.context.portal_catalog(UID=linked)
    return folder[0].getObject()

def small(self):
    small = self.data['small']
    return 100/small

def medium(self):
    medium = self.data['medium']
    return 100/medium

def large(self):
    large = self.data['large']
    return 100/large

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return False
