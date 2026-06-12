#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacao:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Box2")
        janela.set_border_width(10)
        box_vert = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, homogeneous = True, spacing = 10)
        box_hor = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, homogeneous = True, spacing = 10)
        self.lbl_msg = Gtk.Label(label = "---X---")

        mensagens = ["Fé", "Paz", "Amizade", "Coragem", "Esperança"]
        for msg in mensagens:
            bt = Gtk.Button(label = msg)
            bt.connect("clicked", self.exibir_mensagem)
            box_hor.add(bt)

        box_vert.add(box_hor)
        box_vert.add(self.lbl_msg)
        janela.add(box_vert)
        janela.show_all()

    def exibir_mensagem(self, componente = None, dados = None):
        msg = componente.get_label()
        msg = msg.lower()
        msg = "Muita {}!!!".format(msg)
        self.lbl_msg.set_label(msg)

    def sair(self, componentes = None, dados = None):
        Gtk.main_quit()

if __name__ == "__main__":
    prog = Aplicacao()
    Gtk.main()
    