#!/usr/bin/env/python
# -*- coding: utf-8 -*-
from ciscoipphone.base import CiscoService


class MenuItem(CiscoService):
    class Meta:
        service_name = 'MenuItem'
        fields = ['Name', 'URL']


class SoftKeyItem(CiscoService):
    class Meta:
        service_name = 'SoftKeyItem'
        fields = ['Name', 'URL', 'Position']


class ExecuteItem(CiscoService):
    class Meta:
        service_name = 'ExecuteItem'
        fields = ['URL']


class InputItem(CiscoService):
    class Meta:
        service_name = 'InputItem'
        fields = ['DisplayName', 'QueryStringParam', 'DefaultValue',
                  'InputFlags']


class IconItem(CiscoService):
    class Meta:
        service_name = 'IconItem'
        fields = ['Index', 'Width', 'Height', 'Depth', 'Data']


class DirectoryEntry(CiscoService):
    class Meta:
        service_name = 'DirectoryEntry'
        fields = ['Name', 'Telephone']


class Menu(CiscoService):
    class Meta:
        service_name = 'CiscoIPPhoneMenu'
        fields = ['Prompt', 'Title', 'MenuItem']

    def add_item(self, name, url):
        self.items.append(MenuItem(name=name, url=url))


class Directory(CiscoService):
    class Meta:
        service_name = 'CiscoIPPhoneDirectory'
        fields = ['Prompt', 'Title', 'DirectoryEntry', 'SoftKeyItem']

    def add_entry(self, name, telephone):
        self.items.append(DirectoryEntry(name=name, telephone=telephone))

    def add_softkey(self, name, url, position):
        self.items.append(SoftKeyItem(name=name, url=url, position=position))


class Text(CiscoService):
    class Meta:
        service_name = 'CiscoIPPhoneText'
        fields = ['Prompt', 'Title', 'Text', 'SoftKeyItem']

    def add_softkey(self, name, url, position):
        self.items.append(SoftKeyItem(name=name, url=url, position=position))


class Input(CiscoService):
    class Meta:
        service_name = 'CiscoIPPhoneInput'
        fields = ['Prompt', 'Title', 'URL', 'InputItem', 'SoftKeyItem']

    def add_softkey(self, name, url, position):
        self.items.append(SoftKeyItem(name=name, url=url, position=position))

    def add_input(self, display_name, query_string_param, default_value,
                  input_flags):

        input_item = InputItem(display_name=display_name,
                               query_string_param=query_string_param,
                               default_value=default_value,
                               input_flags=input_flags)

        self.items.append(input_item)


class Image(CiscoService):
    class Meta:
        service_name = 'CiscoIPPhoneImage'
        fields = ['Prompt', 'Title', 'LocationX', 'LocationY', 'Width',
                  'Height', 'Depth', 'Data', 'SoftKeyItem']

    def add_softkey(self, name, url, position):
        self.items.append(SoftKeyItem(name=name, url=url, position=position))


class GraphicMenu(CiscoService):
    class Meta:
        service_name = 'CiscoIPPhoneGraphicMenu'
        fields = ['Prompt', 'Title', 'LocationX', 'LocationY', 'Width',
                  'Height', 'Depth', 'Data', 'SoftKeyItem', 'MenuItem']

    def add_softkey(self, name, url, position):
        self.items.append(SoftKeyItem(name=name, url=url, position=position))

    def add_item(self, name, url):
        self.items.append(MenuItem(name=name, url=url))


class IconMenu(CiscoService):
    class Meta:
        service_name = 'CiscoIPPhoneIconMenu'
        fields = ['Prompt', 'Title', 'SoftKeyItem', 'MenuItem', 'IconItem']

    def add_softkey(self, name, url, position):
        self.items.append(SoftKeyItem(name=name, url=url, position=position))

    def add_item(self, name, url):
        self.items.append(MenuItem(name=name, url=url))

    def add_icon_item(self, index, width, height, depth, data):
        self.items.append(IconItem(index=index, width=width, height=height,
                                   depth=depth, data=data))


class Execute(CiscoService):
    class Meta:
        service_name = 'CiscoIPPhoneExecute'
        fields = ['ExecuteItem']

    def add_item(self, url):
        self.items.append(ExecuteItem(url=url))
