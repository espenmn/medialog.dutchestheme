def small(self):
    small = self.data['small']
    return 100/small - 2

def medium(self):
    medium = self.data['medium']
    return 100/medium - 2

def large(self):
    large = self.data['large']
    return 100/large - 2

def sort_on(self):
    sorton = 'modified'
    if 'sort_on' in data.keys():
        sorton = data['sort_on']

    return sorton
