=======
Dinkins
=======

Description
===========

.. image:: https://img.shields.io/pypi/v/ciscoipphone.svg
  :alt: Pypi
  :target: https://pypi.python.org/pypi/ciscoipphone/

.. image:: https://img.shields.io/pypi/pyversions/ciscoipphone.svg
  :alt: Python Versions
  :target: https://pypi.python.org/pypi/ciscoipphone/



A collection of tools and constructors for quickly generating and deploying
Cisco IP phone directory services, like Mayor Dinkins would do. #dinks


Installation
============

1. In a new project folder for your phone services:

.. code:: bash

   $ mkdir myphoneservices
   $ cd myphoneservices

2. Install ``ciscoipphone`` from *pypi*.

.. code:: bash

    $ pip install ciscoipphone

Basic Usage
===========

Generating ``CiscoIPPhoneMenu``
-------------------------------

.. code:: python

    from ciscoipphone.services import Menu
    menu = Menu(prompt="Select a directory")
    menu.add_item("My Contacts", "http://server/directory/contacts")
    menu.add_item("Businesses", "http://server/directory/businesses")
    menu.prettify()

Will render:

.. code:: xml

    <?xml version="1.0" ?>

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



Generating ``CiscoIPPhoneDirectory``
------------------------------------

.. code:: python

    from ciscoipphone.services import Directory
    directory = Directory(prompt='Select a contact', title='My Contacts')
    directory.add_entry('Avon Barksdale', 18442391546)
    directory.add_entry('Stringer Bell', 18993712775)
    directory.add_softkey('Dial', 'SoftKey:Dial', 1)
    directory.prettify()

Will render:

.. code:: xml

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

