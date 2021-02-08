
#!/usr/bin/python

#-*- coding:utf8 -*-


import wx

class TreeFrame(wx.Frame):
    def __init__(self, root):
        values = [  '1',
                    ['2', ['2-1', '2-2', ['2-3', ['2-3-1', '2-3-2']]]],
                    ['3', ['3-1', '3-2']],
                    ['4', ['4-1', '4-2', '4-3']],
                    '5'
                 ]
        wx.Frame.__init__(self, root, -1, u"树形控件", size=(400,400))
        self.tree = wx.TreeCtrl(self)
        root = self.tree.AddRoot("root")
        self.AddTreeNodes(root, values)
        self.tree.Expand(root)

        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollpased, self.tree)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)


    def AddTreeNodes(self, root, values):
        for node in values:
            if type(node) == str:
                self.tree.AppendItem(root, node)
            else:
                item = self.tree.AppendItem(root, node[0])
                self.AddTreeNodes(item, node[1])

    def OnItemExpanded(self,event):
        print("OnItemExpanded: "+self.tree.GetItemText(event.GetItem()))

    def OnItemCollpased(self, event):
        print("OnItemCollpased: "+self.tree.GetItemText(event.GetItem()))

    def OnSelChanged(self, event):
        print("OnSelfChenged: "+self.tree.GetItemText(event.GetItem()))




class MyApp(wx.App):
    def OnInit(self):
        self.frame = TreeFrame(None)
        self.frame.Show()
        return True

app = MyApp()
app.MainLoop()