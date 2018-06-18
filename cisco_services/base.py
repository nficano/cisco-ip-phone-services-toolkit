import os
import json
from pprint import pformat

from xml.dom.minidom import parseString as parse_xml_string
from jinja2 import Environment
from jinja2 import FileSystemLoader

class CiscoIPPhoneService:
    def get_jinja2_env(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(current_dir, 'templates')
        return Environment(
            loader=FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def prettify(self, xml_string):
        xml = parse_xml_string(xml_string)
        return '\n'.join([
            l for l in xml.toprettyxml(indent=' ' * 2).split('\n')
            if l.strip()
        ])

    def render(self):
        jinja2_env = self.get_jinja2_env()
        template = f'{self.__class__.__name__}.j2'
        variables = self.__dict__
        rendered = jinja2_env.get_template(template).render(variables)
        return self.prettify(rendered)

    def __repr__(self):
        obj = json.dumps(self.__dict__, sort_keys=True, indent=2)
        return f'<{self.__class__.__name__} {obj}>'
