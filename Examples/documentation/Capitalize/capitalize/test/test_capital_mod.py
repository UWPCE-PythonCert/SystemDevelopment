#!/usr/bin/env python

"""
test code for capitalize module

can be run with py.test or nosetests
"""

import tempfile
import pytest

from capitalize import capital_mod


# a sample pyteset fixture:
# this one creates a temp file, writes somethign to it, and returns the
# name of that file to the whatever uses the fixture.
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


def test_capitalize_line():
    line = "this is a Line to capitalize"
    expected = "This Is A Line To Capitalize"

    assert capital_mod.capitalize_line(line) == expected


def test_capitalize(test_textfile):
    """ test an actual file """
    # capitalize the file
    capital_mod.capitalize(test_textfile, "sample_text_file_cap.txt")

    # now check it
    with open("sample_text_file_cap.txt", 'U') as infile:
        contents = infile.read()

    expected = """This Is A Really Simple Text File.
It Is Here So That I Can Test The Capitalize Script.

And That's Only There To Try Out Packaging And Documentation.

So There."""

    assert contents.strip() == expected
