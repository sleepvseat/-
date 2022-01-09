import logging
import os
import shutil
import tkinter as tk
import tkinter.filedialog
import subprocess as sp
import tkinter.messagebox
import threading

ffmpegpath=os.path.abspath('.')
ffmpegpaths=ffmpegpath+'\\ffmpegfiles\\bin'
ffmpegpathscmd='set PATH=%PATH%;'+'%s'%ffmpegpaths
os.system(ffmpegpathscmd)

def selectfilePath():
    getpath=tk.filedialog.askopenfilename()
    getpath=getpath.replace(r'/','\\')
    get_path.set(getpath)

def savefilepath():
    savepath=tk.filedialog.askdirectory()
    savepath=savepath.replace(r'/','\\')
    save_path.set(savepath)

def renames():
    number=0
    savepath=save_path.get()
    if savepath=='':
        tk.messagebox.showinfo('tipʾ','the save folder cantnot be empty')
        return
    renames_path=get_path.get()
    ra_path=os.path.dirname(renames_path)+'\\'
    ra_useless,ra_name_type=os.path.splitext(renames_path)
    ra_files=os.listdir(ra_path)
    for a in ra_files:
        number+=1
        oldname=ra_path+a
        newname=savepath+'\\'+str(number)+ra_name_type
        shutil.move(oldname,newname)

def merge():
    b=None
    number=0
    savepath=save_path.get()
    savepaths=savepath+'\\'
    merge_path=get_path.get()
    mergepath,mergefile_type=os.path.splitext(merge_path)
    me_path=os.path.dirname(merge_path)+'\\'
    me_files=os.listdir(me_path)
    for a in me_files:
        if a==me_files[0]:
            b=a
            continue
        b=b+'|'+a
    outname='out'+mergefile_type
    while outname in me_files:
        number+=1
        outname='out'+str(number)+mergefile_type
    outname=savepaths+outname
    os.chdir(me_path)
    merge_cmd='ffmpeg -i "concat:%s" -acodec copy %s' %(b,outname)
    merge_cmdrun=sp.Popen(merge_cmd,shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
    merge_cmdrun.wait()
    print(merge_cmdrun)

def conversion(cfnames,getpath):
    cf_name=cfnames
    a=0
    b=0
    c=0
    savepath=save_path.get()
    while savepath=='':
        tk.messagebox.showinfo('tipʾ','the save folder cantnot be empty')
        return
    savepaths=savepath+'\\'
    filetype='.'+file_type.get()
    uslename, get_nametype= os.path.splitext(getpath)

    cf_path=os.path.dirname(getpath)+'\\'
    cfname=cf_name.replace(get_nametype,'')
    outname=cfname+filetype

    numbername1=str(a)+get_nametype
    while numbername1 in os.listdir(cf_path):
        a+=1
        numbername1=str(a)+get_nametype
    os.rename(cf_path+cf_name,cf_path+numbername1)

    numbername2=str(b)+filetype
    while numbername2 in os.listdir(savepaths):
        b=b+1
        numbername2=str(b)+filetype

    cf_cmd='ffmpeg -i  %s  %s'%(cf_path+numbername1,savepaths+numbername2)
    cf_cmdrun=sp.Popen(cf_cmd,shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
    cf_cmdrun.wait()
    os.rename(cf_path+numbername1,cf_path+cf_name)
    while outname in os.listdir(savepaths):
        c+=1
        outname=cfname+str(c)+filetype
    os.rename(savepaths+numbername2,savepaths+outname)

def conversionfile():
    t.delete('1.0',tk.END)
    getpath=get_path.get()
    cf_name=os.path.basename(getpath)
    conversion(cf_name,getpath)
    t.insert(tk.END, '转换完成')

def conversionfiles():
    t.delete('1.0',tk.END)
    getpath=get_path.get()
    needpath=os.path.dirname(getpath)+'\\'
    works=0
    for i in os.listdir(needpath):
        works+=1
        needworks=len(os.listdir(needpath))
        workpercent=int((works/needworks)*100)
        t.insert(tk.END,'转换中，正在转换'+str(workpercent)+'%'+'\n')
        t.update()
        conversion(i,getpath)
    t.insert(tk.END,'转换完成')

#开了多线程不会发生无响应但是程序变慢
def thread_it(func):
    threads=threading.Thread(target=func)
    threads.setDaemon(True)
    threads.start()

win=tk.Tk()
win.geometry('600x650')
win.title('conversionsformat')
win.configure(bg='MediumTurquoise')
win.resizable(width=False,height=False)

get_path=tk.StringVar()
tk.Label(win,bg='AliceBlue',text='Enter the path to  the file you want to converted').place(x=0,y=10)
tk.Entry(win,width=60,textvariable=get_path).place(x=0,y=30)
tk.Button(win,bg='AliceBlue',text='select the path',command=selectfilePath).place(x=425,y=26)

save_path=tk.StringVar()
tk.Label(win,bg='AliceBlue',text='save the file path').place(x=0,y=50)
tk.Entry(win,width=60,textvariable=save_path).place(x=0,y=75)
tk.Button(win,bg='AliceBlue',text='select the save file path',command=savefilepath).place(x=425,y=71)

tk.Label(win,bg='AliceBlue',text='renamefiles1-2-3-').place(x=0,y=150)
tk.Button(win,text='rename',bg='AliceBlue',command=renames).place(x=300,y=150)

tk.Label(win,bg='AliceBlue',text='merge files').place(x=0,y=200)
tk.Button(win,bg='AliceBlue',text='merge',command=merge).place(x=300,y=200)

file_type=tk.StringVar()
tk.Label(win,bg='AliceBlue',text='Enter the file format you want to converted mp3 mp4').place(x=0,y=250)
tk.Entry(win,width=10,textvariable=file_type).place(x=320,y=250)
tk.Button(win,text='conversion',bg='AliceBlue',command=lambda :thread_it(conversionfile)).place(x=395,y=245)
tk.Button(win,text='Batch conversion',bg='AliceBlue',command=lambda :thread_it(conversionfiles)).place(x=470,y=245)

t=tk.Text(win)
t.place(x=15,y=300)

win.mainloop()