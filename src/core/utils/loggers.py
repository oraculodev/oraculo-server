import json
import logging

DJANGO_ATTR = ['status_code', 'server_time']

ATTR_TO_JSON = ['created', 'filename', 'funcName',
                'levelname', 'module', 'msecs', 'name'] + DJANGO_ATTR


class JSONFormatter(logging.Formatter):

    def format(self, record):

        obj = {}
        for attr in ATTR_TO_JSON:
            if getattr(record, attr, None):
                obj[attr] = getattr(record, attr)
        obj['message'] = getattr(record, 'msg') % getattr(record, 'args')
        return json.dumps(obj)
