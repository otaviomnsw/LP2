#!/usr/bin/env python
# -*- coding: utf-8 -*
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacao:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Ex7")
        janela.set_border_width(10)

        box_ver = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box_hor = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        txe_nome = Gtk.Entry()
        cbt_curso = Gtk.ComboBoxText()
        cb_cert = Gtk.CheckButton()
        bt_salvar = Gtk.Button(label="Salvar")
        lbl_aluno = Gtk.Label(label="---X---")
        bt_salvar.connect("clicked", self.salvar, [lbl_aluno, txe_nome, cbt_curso, cb_cert])

        cbt_curso.append("1", "Info")
        cbt_curso.append("2", "Edif")
        cbt_curso.append("3", "Meca")
        box_hor.add(txe_nome)
        box_hor.add(cbt_curso)
        box_hor.add(cb_cert)
        box_ver.add(box_hor)
        box_ver.add(bt_salvar)
        box_ver.add(lbl_aluno)
        janela.add(box_ver)
        janela.show_all()

    def salvar(self, componente=None, dados=None):
        rotulo = dados[0]
        nome = dados[1].get_text()
        curso = dados[2].get_active_text()
        cert = dados[3].get_active()
        rotulo.set_label(f"Aluno: {nome}\nCurso: {curso}\nCertificado: {cert}")

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

prog = Aplicacao()
Gtk.main()
print("oxi")