import unittest
from utils import parse_tag


class MatchTests(unittest.TestCase):
    def test_parse_tag(self):
        cases = [
            (('extends', ['_base/base.html']), "{% extends '_base/base.html' %}"),
            (('extends', ['_base/base.html']), "{%extends '_base/base.html' %}"),
            (('extends', ['ur base/are belong to us.html']), "{%extends 'ur base/are belong to us.html' %}"),
            (('include', ['_base/base.html']), '{% include "_base/base.html" %}'),
            (('include', ['_base/base.html']), '{%  include "_base/base.html"   %}'),
            (('include', ['_base/base.html']), '{% include "_base/base.html"%}'),
            (('include', ['_base/base.html']), '{%include "_base/base.html"%}'),
            (('include', ['_base/base.html']), ' {%include "_base/base.html"%}'),
            (('include', ['_base/base.html']), 'hnidopich{%include "_base/base.html"%}  '),
            (('include', ['lorem-ipsum/__dolorem']), "    {% include 'lorem-ipsum/__dolorem' %}"),
            (('includeblocks', ['_base/base.html', '_base templates/base.html']),
                "{% includeblocks '_base/base.html' '_base templates/base.html' %}"),
        ]

        for exp, line in cases:
            self.assertEqual(exp, parse_tag(line))

if __name__ == '__main__':
    unittest.main()

