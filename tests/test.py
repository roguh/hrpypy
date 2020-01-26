#!/usr/bin/env python3
import os
import sys
from copy import deepcopy
from unittest.mock import patch

import nose2

sys.path.insert(1, os.path.join(sys.path[0], '..'))


class Test(object):
    @classmethod
    def setUp(cls):
        cls.patched_methods = [
            'ast.dump',
            'ast.get_source_segment',
        ]
        cls.patchers = {
            method: patch(method) for method in cls.patched_methods
        }
        cls.mocks = {
            method: p.start() for method, p in cls.patchers.items()
        }

    @classmethod
    def tearDown(cls):
        for patcher in cls.patchers.values():
            patcher.stop()

    def test_print_error(self):
        from py import print_error
        print_error("test")

        self.mocks['ast.dump'].return_value = 0
        self.mocks['ast.get_source_segment'].return_value = 0
        print_error("", "")
        print_error("", "", "")

    def test_main(self):
        from py import main
        main()


if __name__ == "__main__":
    nose2.main()
