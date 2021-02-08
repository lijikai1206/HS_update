import wx
import yaml
import os
import wx.lib.agw.customtreectrl as CT


class FrameView(wx.Frame):
    def __init__(self):
        super(FrameView, self).__init__(None, title='View_Update', size=(830, 700))
        self.InitUI()
        self.Show()

    def InitUI(self):
        self.panel = wx.Panel(self, -1)

        self.PLAT_fg = wx.CheckBox(self.panel, -1, "PLAT", (20, 10), (40, 20))
        self.FSK_fg = wx.CheckBox(self.panel, -1, "FSK", (75, 10), (40, 20))
        self.NC_fg = wx.CheckBox(self.panel, -1, "FSK-NC", (130, 10), (60, 20))
        self.check_dir = wx.Button(self.panel, -1, "查询升级包", (210, 10), (70, 20))
        self.check_dir.Bind(wx.EVT_BUTTON, self.get_remote_files)

        self.tx = wx.TextCtrl(self.panel, pos=(280, 40), size=(520, 600))

        # self.palt_tree = CT.CustomTreeCtrl(self.panel, -1, pos=(10, 40), size=(260, 150), agwStyle=wx.TR_DEFAULT_STYLE)
        # self.root = self.palt_tree.AddRoot("Plat_path:/Plat/Scirpt", ct_type=1)
        # for y in range(4):
        #     item = self.palt_tree.AppendItem(self.root, "wangjian", ct_type=1)
        # self.palt_tree.ExpandAll()

        self.fsk_tree = CT.CustomTreeCtrl(self.panel, -1, pos=(10, 200), size=(260, 200), agwStyle=wx.TR_DEFAULT_STYLE)
        self.root = self.fsk_tree.AddRoot("DB_path:/FSK/Scirpt", ct_type=1)
        # for y in range(4):
        #     item = self.fsk_tree.AppendItem(self.root, "wangjian", ct_type=1)
        self.fsk_tree.ExpandAll()

        self.nc_tree = CT.CustomTreeCtrl(self.panel, -1, pos=(10, 410), size=(260, 150), agwStyle=wx.TR_DEFAULT_STYLE)
        self.root = self.nc_tree.AddRoot("WEB_path:/FSK/xxxx", ct_type=1)
        # for y in range(4):
        #     item = self.nc_tree.AppendItem(self.root, "wangjian", ct_type=1)
        self.nc_tree.ExpandAll()

    def read_yaml(self):
        yaml_path = '../config/config.yaml'
        with open(yaml_path, 'r') as f:
            cons = yaml.load(f.read())
        print('yaml_config:', cons)
        return cons

    def get_remote_files(self, event):
        cons = self.read_yaml()
        files_a = os.listdir(cons['romote']['plat_path'])
        print(files_a)
        self.palt_tree = CT.CustomTreeCtrl(self.panel, -1, pos=(10, 40), size=(260, 150), agwStyle=wx.TR_DEFAULT_STYLE)
        self.root = self.palt_tree.AddRoot("Plat_path:/Plat/Scirpt", ct_type=1)
        for unit in files_a:
            item = self.palt_tree.AppendItem(self.root, unit, ct_type=1)
        self.palt_tree.ExpandAll()


if __name__ == '__main__':
    app = wx.App()
    FrameView()
    app.MainLoop()