from xml.dom.minidom import Document
import copy

example = {
    'CiscoIPPhoneMenu': {
        'Title': 'Title text goes here',
        'Prompt': 'The prompt text goes here',
        'MenuItem': [
            {
                'Name':'Foo Menu',
                'URL':'http://path-to-foo-menu'
            },
            {
                'Name':'Bar Menu',
                'URL':'http://path-to-bar-menu'
            },
        ]
    }
}

class dict2xml(object):
    doc = Document()

    def __init__(self, structure):
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
