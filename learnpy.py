#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import sys
    import json
    try:
        input = sys.argv[1]
        if type(input) is str:
            input = json.loads(input)
        print(input)
    except Exception as e:
        raise e
