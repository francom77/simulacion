#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.6.7 (standalone edition) on Tue Jun 11 09:44:34 2013
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class PrincipalFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PrincipalFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, ("Simulacion: Remiseria"))
        self.label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, ("Datos:"))
        self.label_2_copy = wx.StaticText(self.panel_1, wx.ID_ANY, ("Cantidad de Remises:"))
        self.remises = wx.SpinCtrl(self.panel_1, wx.ID_ANY, "", min=0, max=100)
        self.label_2_copy_copy = wx.StaticText(self.panel_1, wx.ID_ANY, ("Cantidad de Corridas:"))
        self.Corridas = wx.SpinCtrl(self.panel_1, wx.ID_ANY, "", min=0, max=100)
        self.simular = wx.Button(self.panel_1, wx.ID_ANY, ("Simular"))
        self.graficos = wx.Button(self.panel_1, wx.ID_ANY, ("Ver Graficos..."))
        self.label_2_copy_1 = wx.StaticText(self.panel_1, wx.ID_ANY, ("Resultados:"))
        self.resultados = wx.ListCtrl(self.panel_1, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PrincipalFrame.__set_properties
        self.SetTitle(("Simulacion"))
        self.label_1.SetFont(wx.Font(18, wx.MODERN, wx.NORMAL, wx.BOLD, 0, "Calibri"))
        self.label_2.SetFont(wx.Font(14, wx.MODERN, wx.NORMAL, wx.BOLD, 0, "Calibri"))
        self.label_2_copy.SetMinSize((180, 23))
        self.label_2_copy.SetFont(wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Calibri"))
        self.remises.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.label_2_copy_copy.SetMinSize((180, 23))
        self.label_2_copy_copy.SetFont(wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Calibri"))
        self.Corridas.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.label_2_copy_1.SetFont(wx.Font(14, wx.MODERN, wx.NORMAL, wx.BOLD, 0, "Calibri"))
        self.resultados.SetMinSize((497, 180))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PrincipalFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.label_1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer_2.Add(self.label_2, 0, wx.ALL, 5)
        sizer_3.Add(self.label_2_copy, 0, wx.ALL, 5)
        sizer_3.Add(self.remises, 0, wx.ALL, 5)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_3_copy.Add(self.label_2_copy_copy, 0, wx.ALL, 5)
        sizer_3_copy.Add(self.Corridas, 0, wx.ALL, 5)
        sizer_2.Add(sizer_3_copy, 1, wx.EXPAND, 0)
        sizer_4.Add(self.simular, 0, wx.ALL, 5)
        sizer_4.Add(self.graficos, 0, wx.ALL, 5)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_2.Add(self.label_2_copy_1, 0, wx.ALL, 5)
        sizer_2.Add(self.resultados, 0, wx.ALL | wx.EXPAND, 5)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class PrincipalFrame
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = PrincipalFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()