#!/usr/bin/env python
# -*- coding: utf-8 -*
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacao:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Ex5")
        janela.set_border_width(10)

        box_ver = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box_hor = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl_conver = Gtk.Label(label="---X---")
        bt_euro = Gtk.Button(label="Para Euro")
        bt_dolar = Gtk.Button(label="Para Dólar")
        bt_btcn = Gtk.Button(label="Para Bitcoin")
        txe_real = Gtk.Entry()
        bt_euro.connect("clicked", self.converter, [txe_real, "euro" ,lbl_conver])
        bt_dolar.connect("clicked", self.converter, [txe_real, "dolar", lbl_conver])
        bt_btcn.connect("clicked", self.converter, [txe_real, "bitcoin", lbl_conver])

        box_ver.add(txe_real)
        box_hor.add(bt_euro)
        box_hor.add(bt_dolar)
        box_hor.add(bt_btcn)
        box_ver.add(box_hor)
        box_ver.add(lbl_conver)
        janela.add(box_ver)
        janela.show_all()

    def converter(self, componente=None, dados=None):
        rotulo = dados[2]
        reais = float(dados[0].get_text())
        moeda = dados[1]
        if moeda == "euro":
            rotulo.set_label(str(round(reais/5.90, 3)) + " euro(s)")
        elif moeda == "dolar":
            rotulo.set_label(str(round(reais/5.18, 3)) + " dolar(es)")
        else:
            rotulo.set_label(str(round(reais/310897.59, 3)) + " bitcoin(s)")

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

prog = Aplicacao()
Gtk.main()
print("oxi")