#!/usr/bin/env/python
# -*- coding: utf-8 -*-
from xml.dom.minidom import Document
import re


class DictToXML(object):
    def __init__(self, structure):
        self.doc = Document()
        if len(structure) == 1:
            root_name = str(list(structure.keys())[0])
            self.root = self.doc.createElement(root_name)

            self.doc.appendChild(self.root)
            self.build(self.root, structure[root_name])

    def build(self, parent, structure):
        if isinstance(structure, dict):
            for k in structure:
                tag = self.doc.createElement(k)
                parent.appendChild(tag)
                self.build(tag, structure[k])
        elif isinstance(structure, list):
            grand_parent = parent.parentNode
            tag_name = parent.tagName
            grand_parent.removeChild(parent)
            for s in structure:
                tag = self.doc.createElement(tag_name)
                self.build(tag, s)
                grand_parent.appendChild(tag)
        else:
            data = str(structure)
            tag = self.doc.createTextNode(data)
            parent.appendChild(tag)

    def to_string(self):
        return self.doc.toxml()

    def prettify(self):
        xml = self.doc.toprettyxml(indent='  ')
        regexp = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)
        return regexp.sub('>\g<1></', xml)
