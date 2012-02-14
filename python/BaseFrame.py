# -*- coding: utf-8 -*
import wx
import socket


class BaseFrame(wx.Frame):
    #hote = "10.240.254.168" #adresse ip du mac mini
    port = 12800
    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print "Connexion établie avec le serveur sur le port", port
    def __init__(self, parent, title):
       wx.Frame.__init__(self, parent, title=title, size=(500,400))
       self.initUi()
       self.bindHandlers()
       self.Show(True)

    def initUi(self):
        panel = wx.Panel(self, -1)

        self.textCtrl = wx.TextCtrl(panel, pos=(50, 50), size=(250, 150), style=wx.TE_MULTILINE)
        self.entry = wx.TextCtrl(panel,-1,value=u"",pos=(300, 150),size=(150,20))
        self.button = wx.Button(panel, label="Click me", pos=(300, 50),size=(100,50))
        self.conex = wx.Button(panel, label="Connection", pos=(300, 200),size=(100,50))


    def onButtonClicked(self, event):
        self.textCtrl.AppendText("Clicked! ")
        print "clicked!"
        msg_a_envoyer = "Clique"
        self.connexion_avec_serveur.send(msg_a_envoyer)
        msg_recu = self.connexion_avec_serveur.recv(1024)
        print msg_recu.decode() # là encore, peut planter si y'a des accents

    def onButtonClicked2(self, event):
        hote=self.entry.GetValue()
        self.connexion_avec_serveur.connect((hote, self.port))
    def bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self.onButtonClicked, self.button)
        self.Bind(wx.EVT_BUTTON, self.onButtonClicked2, self.conex)
