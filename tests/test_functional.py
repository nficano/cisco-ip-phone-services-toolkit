from tests.testingutils import compare_xml_strings, get_test_file
from ciscoipphone.services import Menu, Directory

class TestReadme(object):
    def test_generating_ciscoipphonemenu(self, capsys):
        expected = get_test_file('readme_ciscoipphone_expected')

        menu = Menu(prompt="Select a directory")
        menu.add_item("My Contacts", "http://server/directory/contacts")
        menu.add_item("Businesses", "http://server/directory/businesses")
        menu.prettify()
        received, err = capsys.readouterr()

        assert compare_xml_strings(expected, received)

    def test_generating_CiscoIpPhoneDirectory(self, capsys):
        expected = get_test_file('readme_ciscoipphonedirectory_expected')

        directory = Directory(prompt='Select a contact', title='My Contacts')
        directory.add_entry('Avon Barksdale', 18442391546)
        directory.add_entry('Stringer Bell', 18993712775)
        directory.add_softkey('Dial', 'SoftKey:Dial', 1)
        directory.prettify()
        received, err = capsys.readouterr()

        assert compare_xml_strings(expected, received)
