cisco-ip-phone-services
=========================
Python wrapper for developing Cisco IP Phone XML Services. 

I hacked this up in one night, so its extremely crude, BUT I plan on
working on this a lot over the coming days :)

Usage example
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
