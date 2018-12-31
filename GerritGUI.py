# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import re


###########################################################################
## Class GerritGUI
###########################################################################


class GerritGUI(wx.Frame):
    def __init__(self, parent):
        self.RESULTS = ''
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Gerrit GUI by Coc integration&Test Team",
                          pos=wx.DefaultPosition, size=wx.Size(494, 388),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Gerrit urls:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        bSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        gbSizer4 = wx.GridBagSizer(0, 0)
        gbSizer4.SetFlexibleDirection(wx.BOTH)
        gbSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, u"please copy gerrit urls from email\n", wx.DefaultPosition,
                                       wx.Size(300, 60), style=wx.TE_MULTILINE | wx.HSCROLL)
        self.m_textCtrl1.SetToolTipString(u"e.g,  https://androidhub.harman.com/#/c/28282/2")

        gbSizer4.Add(self.m_textCtrl1, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"Current user:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        gbSizer4.Add(self.m_staticText9, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"unknown", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)

        gbSizer4.Add(self.m_staticText11, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer1.Add(gbSizer4, 1, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        m_radioBox1Choices = [u"sanity-test", u"code-review", u"verified"]
        self.m_radioBox1 = wx.RadioBox(self, wx.ID_ANY, u"Action Types", wx.DefaultPosition, wx.DefaultSize,
                                       m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS)
        self.m_radioBox1.SetSelection(0)
        bSizer5.Add(self.m_radioBox1, 0, wx.ALL, 5)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.Size(368, 80),
                                            style=wx.TE_MULTILINE | wx.HSCROLL)
        self.m_staticText13.Wrap(-1)

        bSizer5.Add(self.m_staticText13, 0, wx.ALL, 5)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 5)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_button16 = wx.Button(self, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_button16, 0, wx.ALL, 5)

        self.m_button15 = wx.Button(self, wx.ID_ANY, u"Check", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_button15, 0, wx.ALL, 5)

        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, u"Update gerrit result via SSH, not REST",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)

        fgSizer1.Add(self.m_staticText15, 0, wx.ALL, 5)

        bSizer1.Add(fgSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(1, wx.DEFAULT_STATUSBAR_STYLE, wx.ID_ANY)
        self.m_menubar2 = wx.MenuBar(0)
        self.m_menu2 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"TBD", wx.EmptyString, wx.ITEM_NORMAL)
        # self.m_menu2.Append(self.m_menuItem3, "TTT")
        self.m_menu2.Append(wx.NewId(), "#TODO", "")

        self.m_menubar2.Append(self.m_menu2, u"AboutMe")

        self.SetMenuBar(self.m_menubar2)

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_textCtrl1.Bind(wx.EVT_TEXT, self.m_text_change)
        self.m_staticText11.Bind(wx.EVT_ENTER_WINDOW, self.m_show_user)
        self.m_radioBox1.Bind(wx.EVT_RADIOBOX, self.m_radio_select)
        self.m_staticText13.Bind(wx.EVT_CHAR, self.m_text_change_result)
        self.m_button16.Bind(wx.EVT_BUTTON, self.m_button_run)
        self.m_button15.Bind(wx.EVT_BUTTON, self.m_button_check)
        self.Bind(wx.EVT_MENU, self.m_menu_selected, id=self.m_menuItem3.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_text_change(self, event):
        content = self.m_textCtrl1.GetLabel()
        gerrits = self._get_gerrit_ids(content)
        self.RESULTS += "Gerrits: " + str(gerrits)
        self.m_staticText13.SetLabel(self.RESULTS)

    def m_show_user(self, event):
        ssh_name = self._get_sshname_config()
        self.m_staticText11.SetLabel(ssh_name)

    def m_radio_select(self, event):
        event.Skip()

    def m_text_change_result(self, event, msg):
        # self.m_staticText13.SetLabel(msg)
        self._set_result_value(msg)

    def m_button_run(self, event):
        # self.m_staticText13.SetLabel('sssss')
        self._set_result_value('sss')
        # event.Skip()

    def m_button_check(self, event):
        event.Skip()

    def m_menu_selected(self, event):
        event.Skip()

    def _get_sshname_config(self):
        home_path = os.environ['HOMEPATH']
        if home_path:
            try:
                with open('c:/' + home_path + '\.ssh\config', 'r') as f:
                    lines = f.readlines()
                sshName = lines[-1].split(' ')[-1]
                return sshName
            except Exception as e:
                return "Please check config"
        else:
            return 'Please check config'

    def _get_gerrit_ids(self, ids):
        # list = ids.split('\n')
        # gerrits = []
        # for id in list:
        #     if id:
        #         contents = id.split('/')
        #         if contents[-2].isdigit():
        #             gerrits.append(contents[-2])
        p = re.compile(r'\d{5,8}')
        groups = p.findall(ids, re.I)
        return groups

    def _set_result_value(self, strs):
        self.RESULTS += (str(strs))
        self.RESULTS += (str(strs))
        self.m_staticText13.SetLabel(strs)
