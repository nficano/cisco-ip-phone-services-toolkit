from .base import CiscoIPPhoneService


class CiscoIPPhoneMenu(CiscoIPPhoneService):
    def __init__(self, title, prompt):
        self.title = title
        self.prompt = prompt
        self.menu_items = []

    def add_menu_item(self, name, url):
        self.menu_items.append({
            'name': name,
            'url': url,
        })
        return self


class CiscoIPPhoneText(CiscoIPPhoneService):
    def __init__(self, title, prompt, text):
        self.title = title
        self.prompt = prompt
        self.text = text


class CiscoIPPhoneInput(CiscoIPPhoneService):
    def __init__(self, title, prompt, url):
        self.title = title
        self.prompt = prompt
        self.url = url
        self.input_items = []

    def add_input_item(
        self,
        display_name,
        query_string_param,
        default_value,
        input_flags,
    ):
        self.input_items.append({
            'display_name': display_name,
            'query_string_param': query_string_param,
            'default_value': default_value,
            'input_flags': input_flags,
        })
        return self


class CiscoIPPhoneDirectory(CiscoIPPhoneService):
    def __init__(self, title, prompt):
        self.title = title
        self.prompt = prompt
        self.directory_entries = []

    def add_directory_entry(self, name, telephone):
        self.directory_entries.append({
            'name': name,
            'telephone': telephone,
        })
        return self


class CiscoIPPhoneImage(CiscoIPPhoneService):
    def __init__(
        self, title, prompt, location_x, location_y, width, height,
        depth, data, window_mode='Normal',
    ):
        self.title = title
        self.prompt = prompt
        self.location_x = location_x
        self.location_y = location_y
        self.width = width
        self.height = height
        self.depth = depth
        self.data = data
        self.window_mode = 'Normal'
        self.soft_key_items = []

    def add_soft_key_item(self, name, url, position, url_down=None):
        self.soft_key_items.append({
            'name': name,
            'url': url,
            'position': position,
            'url_down': url_down,
        })
        return self


class CiscoIPPhoneImageFile(CiscoIPPhoneService):
    def __init__(
        self, title, prompt, location_x, location_y, url,
        window_mode='Normal',
    ):
        self.title = title
        self.prompt = prompt
        self.location_x = location_x
        self.location_y = location_y
        self.url = url
        self.window_mode = window_mode


class CiscoIPPhoneGraphicMenu(CiscoIPPhoneService):
    def __init__(
        self, title, prompt, location_x, location_y, width, height,
        depth, data, window_mode='Normal',
    ):
        self.title = title
        self.prompt = prompt
        self.location_x = location_x
        self.location_y = location_y
        self.width = width
        self.height = height
        self.depth = depth
        self.data = data
        self.window_mode = 'Normal'
        self.menu_items = []

    def add_menu_item(self, name, url):
        self.menu_items.append({'name': name, 'url': url})
        return self


class CiscoIPPhoneGraphicFileMenu(CiscoIPPhoneService):
    def __init__(
        self, title, prompt, location_x, location_y, url,
        window_mode='Normal',
    ):
        self.title = title
        self.prompt = prompt
        self.location_x = location_x
        self.location_y = location_y
        self.url = url
        self.window_mode = window_mode
        self.menu_items = []

    def add_menu_item(
        self, name, url, touch_area_x1='left edge',
        touch_area_y1='top edge', touch_area_x2='right edge',
        touch_area_y2='bottom edge',
    ):
        self.menu_items.append({
            'name': name,
            'url': url,
            'touch_area_x1': touch_area_x1,
            'touch_area_y1': touch_area_y1,
            'touch_area_x2': touch_area_x2,
            'touch_area_y2': touch_area_y2,
        })
        return self


class CiscoIPPhoneIconMenu(CiscoIPPhoneService):
    def __init__(self, title, prompt):
        self.title = title
        self.prompt = prompt
        self.menu_items = []
        self.soft_key_items = []
        self.icon_items = []

    def add_menu_item(self, icon_index, name, url):
        self.menu_items.append({
            'icon_index': icon_index,
            'name': name,
            'url': url,
        })
        return self

    def add_soft_key_item(self, name, url, position, url_down=None):
        self.soft_key_items.append({
            'name': name,
            'url': url,
            'position': position,
            'url_down': url_down,
        })
        return self

    def add_icon_item(self, index, height, width, depth, data):
        self.icon_items.append({
            'index': index,
            'height': height,
            'width': width,
            'depth': depth,
            'data': data,
        })
        return self


class CiscoIPPhoneIconFileMenu(CiscoIPPhoneService):
    def __init__(self, title, prompt):
        self.title = title
        self.prompt = prompt
        self.menu_items = []
        self.icon_items = []

    def add_menu_item(self, icon_index, name, url):
        self.menu_items.append({
            'icon_index': icon_index,
            'name': name,
            'url': url,
        })
        return self

    def add_icon_item(self, index, url):
        self.icon_items.append({
            'index': index,
            'url': url,
        })
        return self


class CiscoIPPhoneStatus(CiscoIPPhoneService):
    def __init__(
        self, text, timer, location_x, location_y, width, height,
        depth, data,
    ):
        self.text = text
        self.timer = timer
        self.location_x = location_x
        self.location_y = location_y
        self.width = width
        self.height = height
        self.depth = depth
        self.data = data


class CiscoIPPhoneStatusFile(CiscoIPPhoneService):
    def __init__(self, text, timer, location_x, location_y, url):
        self.text = text
        self.timer = timer
        self.location_x = location_x
        self.location_y = location_y
        self.url = url


class CiscoIPPhoneExecute(CiscoIPPhoneService):
    def __init__(self, url):
        self.url = url


class CiscoIPPhoneResponse(CiscoIPPhoneService):
    def __init__(self, status, data, url):
        self.status = status
        self.data = data
        self.url = url


class CiscoIPPhoneError(CiscoIPPhoneService):
    def __init__(self, number, message=None):
        self.number = number
        self.message = message
