#!/usr/bin/env python

"""
A custom widget to switch between different entries in the address book

Subclassed from a wx.Panel

This version doesn't have a way to switch the panels yet.
  - can you add that?

Maybe buttons for "next" and "back"?
"""

import wx


class Switcher(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        """
        create a new switcher instance.

        :param parent: the parent frame -- this is designed to go on an
                       AddBookFrame object

        :params *args, **kwargs: all the other arguments that a wx.Window takes.
        """
        wx.Panel.__init__(self, parent, *args, **kwargs)

        self.add_book_frame = parent

        # add some widgets here to do the switching

    def onPrev(self, evt=None):
        # save the data in the form
        print("in onPrev")
        self.add_book_frame.previous()

    def onNext(self, evt=None):
        # restore the form
        print("in onNext")
        next(self.add_book_frame)


class TestFrame(wx.Frame):
    """
    simple Frame with just enough to text the Switcher
    """
    def __next__(self):
        print("next() called in frame")

    def previous(self):
        print("previous() called in frame")

# I like to have a little test app so it can be run on its own
if __name__ == "__main__":

    app = wx.App(False)
    f = TestFrame(None)
    p = Switcher(f)
    f.Show()
    app.MainLoop()
