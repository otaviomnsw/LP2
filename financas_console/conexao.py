# -*- coding: utf-8 -*-
import configparser
import certifi
import mysql.connector

#senha né mn 4LF6t2gUVnvEDktT

def conectar():
   """Lê o config.ini e devolve uma conexão aberta e criptografada (TLS)."""

   cfg = configparser.ConfigParser()
   cfg.read("config.ini", encoding="utf-8")
   banco = cfg["banco"]

   return mysql.connector.connect(
       host=banco["host"],
       port=banco.getint("porta"),
       user=banco["usuario"],
       password=banco["senha"],
       database=banco["nome"],
       ssl_ca=certifi.where(),       
       ssl_verify_cert=True,         
       ssl_verify_identity=True,    
   )