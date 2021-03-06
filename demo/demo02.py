#encoding:utf-8
import wx
import wx.lib.agw.customtreectrl as CT


class MyFrame(wx.Frame):
    def __init__(self, parent):

        self.checked_items = []
        wx.Frame.__init__(self, parent, -1, "customtreectrl")
        self.custom_tree = CT.CustomTreeCtrl(self, agwStyle=wx.TR_DEFAULT_STYLE)
        self.root = self.custom_tree.AddRoot("root",  ct_type=1)
        for y in range(5):
            item = self.custom_tree.AppendItem(self.root, "wangjian", ct_type=1)
        self.custom_tree.ExpandAll()

        self.Bind(CT.EVT_TREE_ITEM_CHECKED, self.checked_item)

    def checked_item(self, event):
        # 只要树控件中的任意一个复选框状态有变化就会响应这个函数
        if (event.GetItem() == self.root):
            if self.custom_tree.IsItemChecked(event.GetItem()):
                self.custom_tree.CheckChilds(self.root)
                for item in self.get_childs(self.root):
                    self.checked_items.append(self.custom_tree.GetItemText(item))

            else:
                for item in self.get_childs(self.root):
                    self.custom_tree.CheckItem(item, False)
                    self.checked_items.remove(self.custom_tree.GetItemText(item))

        # else:
        #     if self.custom_tree.IsItemChecked(event.GetItem()):
        #         self.checked_items.append(self.custom_tree.GetItemText(event.GetItem()))
        #         print "add"
        #     else:
        #         self.checked_items.remove(self.custom_tree.GetItemText(event.GetItem()))
        #         print "remove"
        print(self.checked_items)

    def get_childs(self, item_obj):
        item_list = []
        (item, cookie) = self.custom_tree.GetFirstChild(item_obj)
        while item:
            item_list.append(item)
            print("ok")
            (item, cookie) = self.custom_tree.GetNextChild(item_obj, cookie)
        return item_list

app = wx.App()
frame = MyFrame(None)
frame.Show()
app.MainLoop()