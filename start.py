#!/usr/bin/env python

import wx
from ui import widjet


def main():
    app = wx.App()
    frame = widjet.MyFrame()
    app.MainLoop()

if __name__ == "__main__":
   main()
