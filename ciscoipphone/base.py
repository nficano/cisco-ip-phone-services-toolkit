from ciscoipphone.utils import dict2xml

class CiscoServiceOptions(object):
    service_name = None
    fields = ['Prompt', 'Title']

    def __new__(cls, meta=None):
        overrides = {}

        if meta:
            for override_name in dir(meta):
                overrides[override_name] = getattr(meta, override_name)
        return object.__new__(type('CiscoServiceOptions', (cls,), overrides))

class DeclarativeMetaclass(type):
    def __new__(cls, name, bases, attrs):
        new_class = super(DeclarativeMetaclass, cls).__new__(cls, name,
            bases, attrs)
        opts = getattr(new_class, 'Meta', None)
        new_class._meta = CiscoServiceOptions(opts)
        return new_class

class CiscoService(object):
    __metaclass__ = DeclarativeMetaclass

    def __init__(self, **kwargs):
        self.data = {}
        self.items = []
        for key, value in kwargs.items():
            if value:
                setattr(self, key, value)

    def set_field(self, name, value):
        for index, key in enumerate(self._meta.fields):
            if key.lower() == name.lower().replace('_',''):
                if isinstance(value, dict):
                    lst = self.data.get(key, list())
                    lst.append(value)
                    self.data[key] = lst
                else:
                    self.data[key] = value

    def __setattr__(self, name, value):
        self.set_field(name, value)
        self.__dict__[name] = value

    def to_dict(self):
        if self.items:
            for item in self.items:
                if item._meta.service_name in self._meta.fields:
                    self.set_field(item._meta.service_name, item.to_dict())
        return self.data

    def serialize(self):
        return dict2xml({self._meta.service_name: self.to_dict()}).to_string()

    def prettify(self):
        print dict2xml({self._meta.service_name: self.to_dict()}).prettify()
