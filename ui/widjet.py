
import wx
import os
from utils.image_utils import ImageUtil

name_destination=''
format='PNG'
name_from=''


def start_invert(_path):
    progressMax=len(os.listdir(_path))
    dialog = wx.ProgressDialog("A progress box", "Time remaining", progressMax,
        style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
    count = 0
    for files in os.listdir(_path):
        image_path=os.path.join(_path, files)
        name =name_destination+os.sep+image_path.split(os.sep)[len(image_path.split(os.sep)) - 1].split('.')[0]
        ImageUtil(_path=image_path).invert_image().save_image(format=format,image_name=name)
       
        count = count + 1
        dialog.Update(count)
        
    dialog.Destroy()
            


class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Inverse Imaga (alpha)')
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.path_start = wx.TextCtrl(panel)
        self.path_end = wx.TextCtrl(panel)
        
        self.btn_start = wx.Button(panel, label='Folder line', pos=(5, 55))
        self.btn_start.myname = "from"
        self.btn_start.Bind(wx.EVT_BUTTON, self.on_choose_folder,self.btn_start)
            
        self.btn_end = wx.Button(panel, label='Folder save', pos=(5, 55))
        self.btn_end.myname = "to"
        self.btn_end.Bind(wx.EVT_BUTTON, self.on_choose_folder, self.btn_end)
       
        self.save = wx.Button(panel, label='Inverse', pos=(5, 100))
        self.save.myname = "save"
        self.save.Bind(wx.EVT_BUTTON, self.on_save, self.save)
        
        format = ['WEBP', 'PNG']   
        lst = wx.ListBox(panel, size = (100,-1), choices = format, style = wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.on_list_box, lst) 

        sizer.Add(self.path_start, 0, wx.ALL | wx.EXPAND, 5) 
        sizer.Add(self.btn_start, 0, wx.ALL | wx.Left, 5)
        sizer.Add(self.path_end, 0, wx.ALL | wx.EXPAND, 5) 
        sizer.Add(self.btn_end, 0, wx.ALL | wx.Left, 5)
        sizer.Add(lst, 0, wx.Left )
        sizer.Add(self.save, 0, wx.ALL | wx.CENTER, 5)
      
        panel.SetSizer(sizer)
        self.Show()
   
    def on_choose_folder(self, event):
        global name_destination
        global name_from
        name = event.GetEventObject().myname
        dialog_header="Choose Line"
        if name=="from":
            dialog_header="Choose folder line"
        else:
            dialog_header="Choose folder save"

        dlg = wx.DirDialog (None, dialog_header, "",
                    wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        
        if dlg.ShowModal() == wx.ID_CANCEL:
            return   

        pathname = dlg.GetPath()
      
        if name=="from":
            name_from=pathname
            self.path_start.SetValue(pathname)
        else:
            name_destination=pathname
            self.path_end.SetValue(pathname)
    
    def on_list_box(self, event):
       global format
       format=event.GetEventObject().GetStringSelection()
    
    def Close(self, force=False):
        return super().Close(force)
    
    def on_save(self,event):
        if not name_from:
            wx.MessageBox('Choose Folder Line', 'Error', wx.OK | wx.ICON_ERROR)
            return
        if not name_destination:
            wx.MessageBox('Choose Folder Save','Error', wx.OK | wx.ICON_ERROR)
            return
        self.save.Disable()
        self.btn_end.Disable()
        self.btn_start.Disable()
         
        start_invert(git remote add origin https://github.com/KonstantinGridasov/Commander.gitos.path.join(name_from))       
        self.Close()