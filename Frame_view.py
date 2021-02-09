import wx
import yaml
import os
import wx.lib.agw.customtreectrl as CT
from src.file_sftp import SFTP

class FrameView(wx.Frame):
    def __init__(self):
        super(FrameView, self).__init__(None, title='FREM2.0_Update', size=(830, 700))
        self.InitUI()
        self.Show()
        self.read_yaml()

    def InitUI(self):
        self.panel = wx.Panel(self, -1)

        self.check_dir = wx.Button(self.panel, -1, "查询升级包", (20, 10), (70, 20))
        self.update_db = wx.Button(self.panel, -1, "升级数据库", (100, 10), (70, 20))
        # self.PLAT_fg = wx.CheckBox(self.panel, -1, "PLAT", (180, 10), (40, 20))
        self.FSK_fg = wx.CheckBox(self.panel, -1, "FSK", (280, 10), (40, 20))
        self.NC_fg = wx.CheckBox(self.panel, -1, "FSK-NC", (330, 10), (60, 20))
        self.NC_fg = wx.CheckBox(self.panel, -1, "Dispatch2", (400, 10), (80, 20))
        self.update_web = wx.Button(self.panel, -1, "升级应用程序", (500, 10), (80, 20))

        self.check_dir.Bind(wx.EVT_BUTTON, self.get_remote_files)
        self.update_db.Bind(wx.EVT_BUTTON, self.update_db_opration)

        self.tx = wx.TextCtrl(self.panel, pos=(280, 40), size=(520, 600), style=wx.TE_MULTILINE)


    def read_yaml(self):
        yaml_path = './config/config.yaml'
        with open(yaml_path, 'r') as f:
            self.cons = yaml.load(f.read())
        host = self.cons['sftp_server']['host']
        port = self.cons['sftp_server']['port']
        username = self.cons['sftp_server']['username']
        password = self.cons['sftp_server']['password']
        self.sf = SFTP(host, port, username, password)
        self.sf.connect()
        return self.cons, self.sf

    # 绑定查询升级包
    def get_remote_files(self, event):
        # files_list = os.listdir(cons['romote']['plat_path'])
        path_list = self.query_files(self.cons['sftp_server']['plat_path'])
        fsk_list = self.query_files(self.cons['sftp_server']['fsk_path'])
        web_path = self.query_files(self.cons['sftp_server']['web_path'])
        self.tx.AppendText('>>>开始获取平台、FSK、FSK-NC的数据包以及web等应用程序包\r\n')
        self.palt_tree = CT.CustomTreeCtrl(self.panel, -1, pos=(10, 40), size=(260, 100), agwStyle=wx.TR_DEFAULT_STYLE)
        self.root1 = self.palt_tree.AddRoot("Plat_path:/Plat/Scirpt", ct_type=1)
        for unit in path_list[-2:]:
            self.palt_tree.AppendItem(self.root1, unit, ct_type=1)
        self.palt_tree.ExpandAll()

        self.fsk_tree = CT.CustomTreeCtrl(self.panel, -1, pos=(10, 150), size=(260, 320), agwStyle=wx.TR_DEFAULT_STYLE)
        self.root2 = self.fsk_tree.AddRoot("DB_path:/FSK/Scirpt", ct_type=1)
        for unit in fsk_list:
            self.palt_tree.AppendItem(self.root2, unit, ct_type=1)
        self.fsk_tree.ExpandAll()

        self.nc_tree = CT.CustomTreeCtrl(self.panel, -1, pos=(10, 480), size=(260, 150), agwStyle=wx.TR_DEFAULT_STYLE)
        self.root3 = self.nc_tree.AddRoot("WEB_path:/FSK/xxxx", ct_type=1)
        for unit in web_path:
            self.palt_tree.AppendItem(self.root3, unit, ct_type=1)
        self.nc_tree.ExpandAll()

        self.tx.AppendText('>>>获取成功，请勾选对应的包下载或升级！\r\n')

    def query_files(self, path):
        files = self.sf.listdir(path)
        return files

    # 绑定升级数据包
    def update_db_opration(self, event):
        plat_file = self.palt_tree.GetChildren()
        print(plat_file)


if __name__ == '__main__':
    app = wx.App()
    FrameView()
    app.MainLoop()