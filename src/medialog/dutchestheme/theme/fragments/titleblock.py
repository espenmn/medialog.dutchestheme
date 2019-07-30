def titlestructure(self):
    data = self.data
    header =  data['header']
    title = data['titletext']
    return "<%s>%s</%s>""" % (header, title, header)
  