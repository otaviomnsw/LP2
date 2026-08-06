#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_INTERFACE = os.path.join(PASTA, 'conversor.glade')

COTACOES = {
   'Real (BRL)': 1.00,
   'Dólar (USD)': 5.40,
   'Euro (EUR)': 5.90,
   'Libra (GBP)': 6.85,
   'Iene (JPY)': 0.035,
}

class Aplicacao:
   def __init__(self):
       self.construtor = Gtk.Builder()
       self.construtor.add_from_file(ARQUIVO_INTERFACE)
       self.construtor.connect_signals(self)

       self.janela = self.construtor.get_object('jan_principal')

       self.txt_valor = self.construtor.get_object('txt_valor')
       self.cmb_origem = self.construtor.get_object('cmb_origem')
       self.cmb_destino = self.construtor.get_object('cmb_destino')
       self.lbl_resultado = self.construtor.get_object('lbl_resultado')

       self.janela.show_all()

   def converter(self, valor, origem, destino):
       valor_em_reais = valor * COTACOES[origem]
       return valor_em_reais / COTACOES[destino]

   def ao_converter(self, componente=None, dados=None):

       valor = float(self.txt_valor.get_text().replace(',', '.'))

       origem = self.cmb_origem.get_active_text()

       destino = self.cmb_destino.get_active_text()

       resultado = self.converter(valor, origem, destino)

       self.lbl_resultado.set_markup(

           f'<big><b>{resultado:.2f}</b></big>\n'

           f'<small>{valor:.2f} {origem} equivalem a {resultado:.2f} {destino}</small>')

   def ao_inverter(self, componente=None, dados=None):

       origem = self.cmb_origem.get_active()

       destino = self.cmb_destino.get_active()

       self.cmb_origem.set_active(destino)

       self.cmb_destino.set_active(origem)

   def ao_limpar(self, componente=None, dados=None):

       self.txt_valor.set_text('')

       self.lbl_resultado.set_markup('—')

       self.txt_valor.grab_focus()

   def ao_destruir(self, componente=None, dados=None):

       Gtk.main_quit()

if __name__ == '__main__':

   Aplicacao()

   Gtk.main()