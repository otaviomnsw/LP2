#!/usr/bin/env python
# -*- coding: utf-8 -*
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacao:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Ex3")
        janela.set_border_width(10)

        box_ver = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box_hor = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        txf_user = Gtk.Entry()
        bt_entrar = Gtk.Button(label="Entrar")
        txf_pswrd = Gtk.Entry()
        lbl_acesso = Gtk.Label()
        bt_entrar.connect("clicked", self.verificar, [txf_user, txf_pswrd, lbl_acesso])
        txf_pswrd.set_visibility(False)
        txf_pswrd.set_invisible_char("*")
        #("<span color='#FF0000'>Acesso Negado</span>")
        #("<span color='#00FF00'>Acesso Liberado</span>")

        box_hor.add(txf_user)
        box_hor.add(txf_pswrd)
        box_ver.add(box_hor)
        box_ver.add(bt_entrar)
        box_ver.add(lbl_acesso)
        janela.add(box_ver)
        janela.show_all()

    def verificar(self, componente=None, dados=None):
        entrada_pes = dados[0]
        entrada_senh = dados[1]
        rotulo = dados[2]
        tentativa_pes = entrada_pes.get_text()
        tentativa_senh = entrada_senh.get_text()
        if tentativa_pes == "admin" and tentativa_senh == "123":
            rotulo.set_markup("<span color='#00FF00'>Acesso Liberado</span>")
        else:
            rotulo.set_markup("<span color='#FF0000'>Acesso Negado</span>")

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

prog = Aplicacao()
Gtk.main()
print("oxi")