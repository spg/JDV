import wx

class SetIpDialog(wx.Dialog):
    def __init__(self, parent, currentIp):
        super(SetIpDialog, self).__init__(parent=parent,
            title='Ip du robot', size=(250, 200))
        self._parent = parent
        self._currentIp = currentIp
        self._initUi()
        self._bindHandlers()

    def _initUi(self):
        panel = wx.Panel(self, -1, size=(250, 200))
        self._okButton = wx.Button(panel, label="OK", pos=(125, 100), size=(100, 50))
        self._ipTextCtrl = wx.TextCtrl(panel, value=self._currentIp)

    def _bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self._onOkButtonClicked, self._okButton)

    def _onOkButtonClicked(self, event):
        ip = self._ipTextCtrl.GetValue()
        self._parent.setIp(ip)
        self.Destroy()

