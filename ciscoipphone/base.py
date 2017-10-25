#!/usr/bin/env/python
# -*- coding: utf-8 -*-
from ciscoipphone.utils import DictToXML
from six import add_metaclass


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
        new_class = super(DeclarativeMetaclass, cls).__new__(
            cls, name, bases, attrs)
        opts = getattr(new_class, 'Meta', None)
        new_class._meta = CiscoServiceOptions(opts)
        return new_class

@add_metaclass(DeclarativeMetaclass)
class CiscoService(object):

    def __init__(self, **kwargs):
        self.data = {}
        self.items = []
        for key, value in list(kwargs.items()):
            if value:
                setattr(self, key, value)

    def set_field(self, name, value):
        for f in self._meta.fields:
            if f.lower() == name.lower().replace('_', ''):
                if isinstance(value, dict):
                    lst = self.data.get(f, list())
                    lst.append(value)
                    self.data[f] = lst
                else:
                    self.data[f] = value

    def to_dict(self):
        if self.items:
            for item in self.items:
                if item._meta.service_name in self._meta.fields:
                    self.set_field(item._meta.service_name, item.to_dict())
        return self.data

    def serialize(self):
        return DictToXML({self._meta.service_name: self.to_dict()}).to_string()

    def prettify(self):
        print(DictToXML({self._meta.service_name: self.to_dict()}).prettify())

    def __setattr__(self, name, value):
        self.set_field(name, value)
        self.__dict__[name] = value
