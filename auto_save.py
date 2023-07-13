import time
import threading
import wx
import os

class HelloApp(wx.App):
    def OnInit(self):
        return True


def save_hello_to_file(file_name):
    i=0
    a=[]
    c="Hello"
    for i in range(10):
        print(c)
        time.sleep(2)
        a.append(c)
        if flag is not None:
            break
    print("write file")
    with open(file_name, 'w') as file:
        file.write('\n'.join(a))

def set_flag():
    global flag
    while flag is None:
        flag = input("Enter a flag value: ")
        print("Flag set to:", flag)

def execute_save_hello():
    count = 1
    directory = None
    while flag is None:
        if count == 1 or directory is None:
            dialog = wx.DirDialog(None, "Choose Directory to Save Hello File", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dialog.ShowModal() == wx.ID_OK:
                directory = dialog.GetPath()
            else:
                continue
            dialog.Destroy()

        file_name = os.path.join(directory, f"hello_{count}.txt")
        save_hello_to_file(file_name)
        count += 1

# Initialize flag
flag = None

# Create wx.App object
app = HelloApp()

# Create threads for each function
save_hello_thread = threading.Thread(target=execute_save_hello)
set_flag_thread = threading.Thread(target=set_flag)

# Start the threads
save_hello_thread.start()
set_flag_thread.start()

app.MainLoop()
