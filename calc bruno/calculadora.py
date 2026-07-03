#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Contas:
    def __init__(self, a):
        self.a = a

    def adcionarNum(self, b):
        self.a = str(self.a) + str(b)
    def mostrarNum(self):
        return self.a
    def mudarNum(self, b):
        self.a = b
    def somar(self,b):
        self.a = float(self.a) + b
    def subtrair(self, b):
        return self.a - b
    def multiplicar(self, b):
        return self.a*b
    def dividir(self, b):
        return self.a/b
    def raizQuad(self):
        return self.a**0.5

visor1 = Contas(0)
visor2 = Contas(0)

class Aplicacao:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Calculadora")
        janela.set_border_width(10)
        box_vert = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, homogeneous = True, spacing = 10)
        self.visorAtual = visor1
        self.ultimaOper = ""
        self.terqir = True

        #caixas -- 
        visor = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, homogeneous = True, spacing = 10)
        boxh1 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, homogeneous = True, spacing = 10)
        boxh2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, homogeneous = True, spacing = 10)
        boxh3 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, homogeneous = True, spacing = 10)
        boxh4 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, homogeneous = True, spacing = 10)
        boxh5 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, homogeneous = True, spacing = 10)

        #label
        lblVisor = Gtk.Label(label=self.visorAtual.mostrarNum())

        #botoes -- 
        btnON = Gtk.Button(label="ON")
        btnClear = Gtk.Button(label="C")
        btnRaiz = Gtk.Button(label="√")
        btnN7 = Gtk.Button(label="7")
        btnN8 = Gtk.Button(label="8")
        btnN9 = Gtk.Button(label="9")
        btnSomar = Gtk.Button(label="+")
        btnN4 = Gtk.Button(label="4")
        btnN5 = Gtk.Button(label="5")
        btnN6 = Gtk.Button(label="6")
        btnSubtrair = Gtk.Button(label="-")
        btnN1 = Gtk.Button(label="1")
        btnN2 = Gtk.Button(label="2")
        btnN3 = Gtk.Button(label="3")
        btnMultiplicar = Gtk.Button(label="*")
        btnN0 = Gtk.Button(label="0")
        btnIgual = Gtk.Button(label="=")
        btnDividir = Gtk.Button(label="/")

        #connectar botoes
        btnN0.connect("clicked", self.colocarNum, [0, lblVisor, self.visorAtual])
        btnN1.connect("clicked", self.colocarNum, [1, lblVisor, self.visorAtual])
        btnN2.connect("clicked", self.colocarNum, [2, lblVisor, self.visorAtual])
        btnN3.connect("clicked", self.colocarNum, [3, lblVisor, self.visorAtual])
        btnN4.connect("clicked", self.colocarNum, [4, lblVisor, self.visorAtual])
        btnN5.connect("clicked", self.colocarNum, [5, lblVisor, self.visorAtual])
        btnN6.connect("clicked", self.colocarNum, [6, lblVisor, self.visorAtual])
        btnN7.connect("clicked", self.colocarNum, [7, lblVisor, self.visorAtual])
        btnN8.connect("clicked", self.colocarNum, [8, lblVisor, self.visorAtual])
        btnN9.connect("clicked", self.colocarNum, [9, lblVisor, self.visorAtual])
        btnSomar.connect("clicked", self.operacao, ["somar", lblVisor, self.visorAtual])

        visor.pack_end(lblVisor, expand=False, fill=False, padding=10)
        boxh2.add(btnN7)
        boxh2.add(btnN8)
        boxh2.add(btnN9)
        boxh2.add(btnSomar)
        boxh3.add(btnN4)
        boxh3.add(btnN5)
        boxh3.add(btnN6)
        boxh3.add(btnSubtrair)
        boxh4.add(btnN1)
        boxh4.add(btnN2)
        boxh4.add(btnN3)
        boxh4.add(btnMultiplicar)
        boxh5.add(btnN0)
        boxh5.add(btnIgual)
        boxh5.add(btnDividir)
        box_vert.add(visor)
        box_vert.add(boxh1)
        box_vert.add(boxh2)
        box_vert.add(boxh3)
        box_vert.add(boxh4)
        box_vert.add(boxh5)
        janela.add(box_vert)
        janela.show_all()

    def colocarNum(self, componentes = None, dados = None):
        num = dados[0]
        lblvisor = dados[1]

        if self.visorAtual.mostrarNum() == 0:
            self.visorAtual.mudarNum(num)
        elif len(str(self.visorAtual.mostrarNum())) < 12:
            self.visorAtual.adcionarNum(num)
        lblvisor.set_label(str(self.visorAtual.mostrarNum()))
    
    def operacao(self, componentes = None, dados = None):
        visor = dados[1]
        operacao = dados[0]

        if self.visorAtual == visor1:
            visor.set_label(str(visor2.mostrarNum()))
            self.visorAtual = visor2
            self.ultimaOper = operacao
        else:
            if self.ultimaOper == "somar":
                self.visorAtual = visor1
                self.visorAtual.somar(float(visor2.mostrarNum()))
                visor.set_label(str(visor1.mostrarNum()))
                visor2.mudarNum(0)
                print("x")

    def sair(self, componentes = None, dados = None):
        Gtk.main_quit()

if __name__ == "__main__":
    prog = Aplicacao()
    Gtk.main()