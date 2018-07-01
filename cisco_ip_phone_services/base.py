import json
import os
from xml.dom.minidom import parseString as parse_xml_string

from jinja2 import Environment
from jinja2 import FileSystemLoader


class CiscoIPPhoneService:
    def render(self, encoding='utf-8'):
        xml = self._strip_newlines(self._render_template())
        return parse_xml_string(xml).toprettyxml(
            indent='',
            newl='',
            encoding=encoding,
        )

    def toprettyxml(self):
        xml = parse_xml_string(self._render_template())
        return '\n'.join([
            l for l in xml.toprettyxml(indent=' ' * 2).split('\n')
            if l.strip()
        ])

    def _get_jinja2_env(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(current_dir, 'templates')
        return Environment(
            loader=FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def _strip_newlines(self, s):
        return ''.join([l.strip() for l in s.split('\n')])

    def _xml_escape(self, s):
        transforms = (
            ('\'', '&apos;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;'),
        )
        for old, new in transforms:
            s = s.replace(old, new)
        return s

    def _render_template(self):
        jinja2_env = self._get_jinja2_env()
        template = f'{self.__class__.__name__}.j2'
        variables = {
            k: self._xml_escape(v) for k, v in self.__dict__.items()
            if isinstance(v, str)
        }

        return jinja2_env.get_template(template).render(variables)

    def __repr__(self):
        obj = json.dumps(self.__dict__, sort_keys=True, indent=2)
        return f'<{self.__class__.__name__} {obj}>'
