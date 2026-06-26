#!/usr/bin/env python
# -*- coding: utf-8 -*
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacao:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Ex6")
        janela.set_border_width(10)

        box_ver = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box_hor = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        txe_nota1 = Gtk.Entry()
        txe_nota2 = Gtk.Entry()
        txe_nota3 = Gtk.Entry()
        txe_rec = Gtk.Entry()
        lbl_passar = Gtk.Label(label="---X---")
        bt_calc = Gtk.Button(label="Calcular")
        bt_calc.connect("clicked", self.calcular, [lbl_passar, txe_nota1, txe_nota2, txe_nota3, txe_rec, box_ver, janela])

        box_hor.add(txe_nota1)
        box_hor.add(txe_nota2)
        box_hor.add(txe_nota3)
        box_hor.add(bt_calc)
        box_ver.add(box_hor)
        box_ver.add(lbl_passar)
        janela.add(box_ver)
        janela.show_all()

    def calcular(self, componente=None, dados=None):
        rotulo = dados[0]
        nota1 = float(dados[1].get_text())
        nota2 = float(dados[2].get_text())
        nota3 = float(dados[3].get_text())
        rec = dados[4]
        cx = dados[5]
        if rec.is_visible():
            if (nota1 + nota2 + nota3 + float(rec.get_text()))/4 >= 6:
                rotulo.set_label("Aprovado")
            else:
                rotulo.set_label("Reprovado")
        else:
            if (nota1 + nota2 + nota3)/3 >= 6:
                rotulo.set_label("Aprovado")
            else:
                cx.add(rec)
                rotulo.set_label("Digite a nota da recuperação")
                dados[6].show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

prog = Aplicacao()
Gtk.main()
print("oxi")