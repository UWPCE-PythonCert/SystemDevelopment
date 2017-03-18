#!/usr/bin/env python

"""
The basic formm for the address book

This gets a Panel to itself
"""

import wx


class AddBookForm(wx.Panel):
    def __init__(self, fields, a_entry, *args, **kwargs):
        """
        create a new AddBookForm

        :param a_entry: a dict for the address book entry
        """
        wx.Panel.__init__(self, *args, **kwargs)

        self._entry = a_entry

        # use a FlexGridSizer:
        S = wx.FlexGridSizer(rows=0, cols=2, vgap=8, hgap=8)
        S.AddGrowableCol(idx=1, proportion=1)

        # create text boxes to edit: first name, last name, phone, email.
        self.inputs = {}
        for name in fields:
            self.inputs[name] = wx.TextCtrl(self)
            S.Add(wx.StaticText(self, label=name), 0,
                  wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
            S.Add(self.inputs[name], flag=wx.EXPAND)

        # Save and Cancel buttons
        sav_but = wx.Button(self, label="Save Record")
        sav_but.Bind(wx.EVT_BUTTON, self.onSave)
        can_but = wx.Button(self, label="Reset Record")
        can_but.Bind(wx.EVT_BUTTON, self.onCancel)

        # a sizer for the buttons:
        but_sizer = wx.BoxSizer(wx.HORIZONTAL)
        but_sizer.Add((1, 1), 1)  # stretchable spave to shift buttons right
        but_sizer.Add(can_but, 0, wx.ALL, 4)
        but_sizer.Add(sav_but, 0, wx.ALL, 4)

        # Put the whole thing in another sizer to
        # layout the buttons...
        outer_sizer = wx.BoxSizer(wx.VERTICAL)
        outer_sizer.Add(S, 0, wx.ALL | wx.EXPAND, 10)
        outer_sizer.Add(but_sizer, 0, wx.EXPAND | wx.RIGHT, 10)
        self.SetSizerAndFit(outer_sizer)

        self.load_data()

    def onSave(self, evt=None):
        # save the data in the form
        self.save_data()

    def onCancel(self, evt=None):
        # restore the form
        self.load_data()

    def _get_entry(self, entry):
        return self._entry

    def _set_entry(self, entry):
        self._entry = entry
        self.load_data()

    entry = property(_get_entry, _set_entry)

    def load_data(self):
        """
        load the data into the form from the data dict
        """
        data = self._entry
        for key in data:
            self.inputs[key].Value = data.setdefault(key, "")

    def save_data(self):
        """
        save the data from the form from the data dict
        """
        data = self._entry
        for key in data:
            data[key] = self.inputs[key].Value


# I like to have a little test app so it can be run on its own
if __name__ == "__main__":

    import address_book_data
    fields = address_book_data.AddressBook.fields

    # a sample entry:
    entry = {'email': 'PythonCHB@gmail.com',
             'First Name': 'Chris',
             'Last Name': 'Barker',
             'Phone': '123-456-7890'}

    app = wx.App(False)
    f = wx.Frame(None)
    p = AddBookForm(fields, entry, f)
    f.Show()
    app.MainLoop()
