# -*- coding: utf-8 -*-

import os
import GerritGUI


def main():
    app = GerritGUI.wx.App(False)
    frame = GerritGUI.GerritGUI(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()


if __name__ == "__main__":
    main()
