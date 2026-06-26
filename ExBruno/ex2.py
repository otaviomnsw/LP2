#!/usr/bin/env python
# -*- coding: utf-8 -*
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacao:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Ex2")
        janela.set_border_width(10)

        self.x = 0
        bt_la = Gtk.Button(label="Clique aqui!")
        lbl_la = Gtk.Label(str(self.x))
        bt_la.connect("clicked", self.aumentar, lbl_la)
        box_ver = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box_hor = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        box_hor.add(lbl_la)
        box_hor.add(bt_la)
        box_ver.add(box_hor)
        janela.add(box_ver)
        janela.show_all()

    def aumentar(self, componente=None, dados=None):
        rotulo = dados
        self.x += 1
        rotulo.set_label(str(self.x))

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

prog = Aplicacao()
Gtk.main()
print("oxi")