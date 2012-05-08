from xml.etree.ElementTree import Element, SubElement, tostring

class CiscoIPPhone(object):   
    def __init__(self, title=None, prompt=None):
        self.softkeys = []
        self.title = title
        self.prompt = prompt

    def add_softkey(self, name, url, position):
        self.softkeys.append({'Name':name, 'URL': url, 'Position:': position})

    def to_xml(self):
        root = Element(self.name)
        title = SubElement(root, 'Title')
        title.text = self.title
        prompt = SubElement(root, 'Prompt')
        prompt.text = self.prompt
        if self.softkeys:
            for softkey in self.softkeys:
                softkey = SubElement(root, 'SoftKeyItem')
                for key, value in softkey.items():
                    item = SubElement(softkey, key)
                    item.text = value
        return root

class Menu(CiscoIPPhone):
    name = 'CiscoIPPhoneMenu'
    
    def __init__(self, *args, **kwargs):
        super(Menu, self).__init__(*args, **kwargs)
        self.items = []

    def add_menu(self, name, url):
        self.items.append({'Name':name, 'URL': url})

    def to_xml(self):
        xml = super(Menu, self).to_xml()
        for i in self.items:
            i = SubElement(xml, 'MenuItem')
            for key, value in i.items():
                item = SubElement(i, key)
                item.text = value
        return tostring(xml)        

class Directory(CiscoIPPhone):
    name = 'CiscoIPPhoneDirectory'
    
    def __init__(self, *args, **kwargs):
        super(Directory, self).__init__(*args, **kwargs)
        self.items = []

    def add_entry(self, name, phone_number):
        self.items.append({'Name':name, 'Telephone': phone_number})

class Text(CiscoIPPhone):
    name = 'CiscoIPPhoneText'


class Input(CiscoIPPhone):
    name = 'CiscoIPPhoneInput'


class Image(CiscoIPPhone):
    name = 'CiscoIPPhoneImage'


class GraphicMenu(CiscoIPPhone):
    name = 'CiscoIPPhoneGraphicMenu'


class IconMenu(CiscoIPPhone):
    name = 'CiscoIPPhoneIconMenu'



