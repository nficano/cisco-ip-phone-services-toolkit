cisco-ip-phone-services
=========================
Python wrapper for developing Cisco IP Phone XML Services. 

Highly work-in-progress!! I hacked this up literally in a single night. It has
a far ways to go before it could be considered usable. 

I really hope to work on this a lot over the coming days/weeks.

USAGE EXAMPLES
-------------
The following are a few usage examples..

CiscoIPPhoneMenu
-------------
::

    >>> from ciscoipphone.services import Menu
    >>> menu = Menu(prompt="Select a directory")
    >>> menu.add_item("My Contacts", "http://server/directory/contacts")
    >>> menu.add_item("Businesses", "http://server/directory/businesses")
    >>> menu.prettify()
    <CiscoIPPhoneMenu>
      <MenuItem>
        <URL>http://server/directory/contacts</URL>
        <Name>My Contacts</Name>
      </MenuItem>
      <MenuItem>
        <URL>http://server/directory/businesses</URL>
        <Name>Businesses</Name>
      </MenuItem>
      <Prompt>Select a directory</Prompt>
    </CiscoIPPhoneMenu>

CiscoIPPhoneDirectory
-------------
::

    >>> from ciscoipphone.services import Directory
    >>> directory = Directory(prompt='Select a contact', title='My Contacts')
    >>> directory.add_entry('Avon Barksdale', 18442391546)
    >>> directory.add_entry('Stringer Bell', 18993712775)
    >>> directory.add_softkey('Dial', 'SoftKey:Dial', 1)
    >>> directory.prettify()
    <?xml version="1.0" ?>
    <CiscoIPPhoneDirectory>
      <DirectoryEntry>
        <Telephone>18442391546</Telephone>
        <Name>Avon Barksdale</Name>
      </DirectoryEntry>
      <DirectoryEntry>
        <Telephone>18993712775</Telephone>
        <Name>Stringer Bell</Name>
      </DirectoryEntry>
      <SoftKeyItem>
        <URL>SoftKey:Dial</URL>
        <Position>1</Position>
        <Name>Dial</Name>
      </SoftKeyItem>
      <Prompt>Select a contact</Prompt>
      <Title>My Contacts</Title>
    </CiscoIPPhoneDirectory>
