#!/usr/bin/env python
# -*- coding: utf-8 -*
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacao:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Ex4")
        janela.set_border_width(10)

        box_ver = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box_hor = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        txf_peso = Gtk.Entry()
        txf_altura = Gtk.Entry()
        bt_calc = Gtk.Button(label="Calcular")
        lbl_imc = Gtk.Label(label="IMC")
        lbl_clasf = Gtk.Label(label="Classificação")
        bt_calc.connect("clicked", self.calcular, [lbl_imc, lbl_clasf, txf_altura, txf_peso])

        box_hor.add(txf_altura)
        box_hor.add(txf_peso)
        box_ver.add(box_hor)
        box_ver.add(bt_calc)
        box_ver.add(lbl_imc)
        box_ver.add(lbl_clasf)
        janela.add(box_ver)
        janela.show_all()

    def calcular(self, componente=None, dados=None):
        rot_imc = dados[0]
        rot_clasf = dados[1]
        entrd_alt = dados[2].get_text()
        entrd_peso = dados[3].get_text()
        try:
            alt = float(entrd_alt)
            peso = float(entrd_peso)
            if peso / alt**2 < 18.5:
                rot_clasf.set_label("Abaixo do peso")
            elif peso / alt**2 < 24.9:
                rot_clasf.set_label("Peso normal")
            elif peso / alt**2 < 29.9:
                rot_clasf.set_label("Sobrepeso")
            elif peso / alt**2 < 34.9:
                rot_clasf.set_label("Obesidade Grau I")
            elif peso / alt**2 < 39.9:
                rot_clasf.set_label("Obesidade Grau II")
            else:
                rot_clasf.set_label("Obesidade Grau III")
            rot_imc.set_label(str(peso/alt**2))
        except:
            rot_imc.set_label("PRECISA SER UM NÚMERO")
            rot_clasf.set_label("PRECISA SER UM NÚMERO")

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

prog = Aplicacao()
Gtk.main()
print("oxi")