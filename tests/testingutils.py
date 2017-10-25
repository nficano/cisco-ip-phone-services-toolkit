import os

import xmltodict


def list_equal(list1, list2):
    for i in list1:
        try:
            list2_index = list2.index(i)
            i2 = list2[list2_index]
        except IndexError:
            return False

        if isinstance(i, dict):
            if not dictionary_equal(i, i2):
                return False
            else:
                continue

        if isinstance(i, list):
            if not list_equal(i, i2):
                return False
            else:
                continue

        if i != i2:
            return False
    return True


def dictionary_equal(dict1, dict2):
    for key, value in dict1.items():
        # Check if we can even get element
        try:
            dict2value = dict2[key]
        except KeyError:
            return False

        # If another dictionary loop
        if isinstance(value, dict) and isinstance(dict2value, dict):
            if not dictionary_equal(value, dict2value):
                return False
            else:
                continue

        # If list send to list equal comparator
        if isinstance(value, list) and isinstance(dict2value, list):
            if not list_equal(value, dict2value):
                return False
            else:
                continue

        # Must be regular value lets compare
        if value != dict2value:
            return False

    return True


def compare_xml_strings(xmls1, xmls2):
    xmldict_1 = xmltodict.parse(xmls1, encoding='utf8', dict_constructor=dict)
    xmldict_2 = xmltodict.parse(xmls2, encoding='utf8', dict_constructor=dict)

    if dictionary_equal(xmldict_1, xmldict_2):
        return True
    else:
        return False


def get_path(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    return path


def get_test_file(filename):
    with open(get_path(filename), 'r') as file:
        return file.read()
