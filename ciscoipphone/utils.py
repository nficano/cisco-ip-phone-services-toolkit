from xml.dom.minidom import Document
import re
import copy

class dict2xml(object):
    def __init__(self, structure):
        self.doc = Document()
        if len(structure) == 1:
            rootName = str(structure.keys()[0])
            self.root = self.doc.createElement(rootName)

            self.doc.appendChild(self.root)
            self.build(self.root, structure[rootName])

    def build(self, father, structure):
        if type(structure) == dict:
            for k in structure:
                tag = self.doc.createElement(k)
                father.appendChild(tag)
                self.build(tag, structure[k])
        
        elif type(structure) == list:
            grandFather = father.parentNode
            tagName = father.tagName
            grandFather.removeChild(father)
            for l in structure:
                tag = self.doc.createElement(tagName)
                self.build(tag, l)
                grandFather.appendChild(tag)
        else:
            data = str(structure)
            tag = self.doc.createTextNode(data)
            father.appendChild(tag)
    
    def to_string(self):
        return self.doc.toxml()

    def prettify(self):
        xml = self.doc.toprettyxml(indent='  ')
        regexp = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)
        return regexp.sub('>\g<1></', xml)
        
        
