#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_INTERFACE = os.path.join(PASTA, 'sla.glade')

class Aplicacao:
    def __init__(self):
        self.construtor = Gtk.Builder()
        self.construtor.add_from_file(ARQUIVO_INTERFACE)
        self.construtor.connect_signals(self)

        self.janela = self.construtor.get_object('jan_prin')
        self.lbl_msg = self.construtor.get_object('lbl_msg')

        self.janela.show_all()

    def Oi(self, componente=None, dados=None):
        self.lbl_msg.set_text('Olá, Mundo!!')
    
    def fechar(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == "__main__":
    Aplicacao()
    Gtk.main()