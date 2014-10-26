#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (c) 2013 Qin Xuye <qin@qinxuye.me>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Created on 2013-5-23

@author: Heway
'''

import json

class MessageKeyEmptyError(Exception):pass


class Message(object):
    def __init__(self, data):
        self.data = dict()

        if isinstance(data, basestring):
            self.data['key'] = data
        elif isinstance(data, unicode):
            self.data['key'] = data.encode(encoding='utf-8')
        elif isinstance(data,dict):
            for key, value in data.items():
                if isinstance(key, unicode):
                    key = key.encode(encoding='utf-8')
                if isinstance(value, unicode):
                    value = value.encode(encoding='utf-8')
                self.data[key] = value
        else:
            raise MessageKeyEmptyError()

    @staticmethod
    def from_str(json_str):
        json_dict = json.loads(json_str)
        return Message(json_dict)

    def __str__(self):
        return json.dumps(self.data)

    def get_key(self):
        return self.get("key")

    def get(self, key):
        return self.data.get(key, None)


if __name__ == '__main__':
    m = Message.from_str(str(Message('12345')))

    print str(m)