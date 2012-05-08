from ciscoipphone.utils import dict2xml
from types import NoneType

class Serializable(object):
    def __init__(self, *args, **kwargs):
        self.data = dict()

    @property
    def name(self):
        return self.__class__.__name__

    def to_dict(self):
        return self.__dict__

class MenuItem(Serializable):
    def __init__(self, name, url):
        setattr(self, 'Name', name)
        setattr(self, 'URL', url)

class CiscoIPPhoneObject(Serializable):
    def __init__(self, title=None, prompt=None):
        self.items = list()
        setattr(self, 'Title', title)
        setattr(self, 'Prompt', prompt)

    def to_dict(self):
        dct = dict()
        for key, val in self.__dict__.items():
            if isinstance(val, list) and len(val):
                for i in val:
                    lst = dct.get(i.name, list())
                    if isinstance(i, MenuItem):
                        lst.append(i.to_dict())
                    dct[i.name] = lst
            if isinstance(val, str):
                dct[key] = val
        return {self.name: dct}

class CiscoIPPhoneMenu(CiscoIPPhoneObject):
    def __init__(self, *args, **kwargs):
        super(CiscoIPPhoneMenu, self).__init__(*args, **kwargs)

    def add_menu(self, name, url):
        self.items.append(MenuItem(name, url))

    def to_dict(self):
        return super(CiscoIPPhoneMenu, self).to_dict()
