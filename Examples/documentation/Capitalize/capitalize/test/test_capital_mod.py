#!/usr/bin/env python

"""
test code for capitalize module

can be run with py.test or nosetests
"""

import tempfile
import pytest

import capitalize
from capitalize import capital_mod

print capitalize.__file__


@pytest.fixture
def test_textfile():
    f = tempfile.NamedTemporaryFile(mode='w',
                                    encoding='utf-8',
                                    newline=None,
                                    delete=False)
    f.write("""This is a really simple Text file.
It is here so that I can test the capitalize script.

And that's only there to try out packaging and documentation.

So there.
"""
)

    return f.name


def test_init():
    """ makes sure it imports and can be read"""
    import capitalize
    assert hasattr(capitalize, '__version__')


def test_capitalize_line():
    line =     "this is a Line to capitalize"
    expected = "This Is A Line To Capitalize"

    assert capital_mod.capitalize_line(line) == expected


def test_capitalize():
    """ test an actual string """
    capital_mod.capitalize("sample_text_file.txt", "sample_text_file_cap.txt")
    contents = open("sample_text_file_cap.txt", 'U').read()
    expected = """This Is A Really Simple Text File.
It Is Here So That I Can Test The Capitalize Script.

And That's Only There To Try Out Distutils.

So There."""
    assert contents.strip() == expected



