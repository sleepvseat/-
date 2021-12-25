import os
import shutil
import tkinter as tk
import tkinter.filedialog
import subprocess as sp
import tkinter.messagebox

#布置环境变量
ffmpegfilepath=os.getcwd()
ffmpegfilepath=ffmpegfilepath+r'\ffmpegfiles\bin'
cmd='path=%path%;'+ffmpegfilepath
os.system(cmd)




def selectfilePath():
    getpath=tk.filedialog.askopenfilename()
    getpath=getpath.replace(r'/','\\')
    get_path.set(getpath)



def savefilepath():
    savepath=tk.filedialog.askdirectory()
    savepath=savepath.replace(r'/','\\')
    save_path.set(savepath)

#重命名文件
def renames():
    number=0
    savepath=save_path.get()
    if savepath=='':
        tk.messagebox.showinfo('提示','保存文件夹不能为空')
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
#合并文件
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
    print(merge_cmdrun)


def conversionfile():
    number=0
    savepath=save_path.get()
    while savepath=='':
        tk.messagebox.showinfo('提示','保存文件路径不能为空')
        return
    savepaths=savepath+'\\'
    filetype='.'+file_type.get()
    getpath=get_path.get()
    uslename, get_nametype= os.path.splitext(getpath)
    cf_name=os.path.basename(getpath)
    cf_path=os.path.dirname((getpath))+'\\'
    cfname=cf_name.replace(get_nametype,'')
    outname=cfname+filetype
    cf_files = os.listdir(savepaths)
    while outname in cf_files:
        number+=1
        outname=str(number)+outname
    outname_path=savepaths+outname
    os.chdir(cf_path)
    cf_cmd='ffmpeg -i  %s  %s'%(cf_name,outname_path)
    cf_cmdrun=sp.Popen(cf_cmd,shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
    print(cf_cmdrun)


def conversionfiles():
    savepath=save_path.get()
    if savepath=='':
        tk.messagebox.showinfo('提示','保存文件夹不能为空')
        return
    savepaths=savepath+'\\'
    filetype=file_type.get()
    filetype='.'+filetype
    getpath=get_path.get()
    cfs_path=os.path.dirname(getpath)+'\\'
    cfs_files=os.listdir(cfs_path)
    for i in cfs_files:
        number = 0
        cfs_name=os.path.splitext(i)[0]
        outname=cfs_name+filetype
        while outname in os.listdir(savepaths):
            number+=1
            outname=str(number)+cfs_name
        outnames=savepaths+outname
        os.chdir(cfs_path)
        cfs_cmd='ffmpeg -i  %s  %s'%(i,outnames)
        cfs_cmdrun=sp.Popen(cfs_cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
        print(cfs_cmdrun)




win=tk.Tk()
win.geometry('600x800')
win.title('conversionsformat')

get_path=tk.StringVar()
tk.Label(win,text='打开文件路径').place(x=0,y=10)
tk.Entry(win,width=60,textvariable=get_path).place(x=80,y=10)
tk.Button(win,text='选择打开文件',command=selectfilePath).place(x=450,y=6)

save_path=tk.StringVar()
tk.Label(win,text='存放文件路径').place(x=0,y=50)
tk.Entry(win,width=60,textvariable=save_path).place(x=80,y=50)
tk.Button(win,text='保存文件路径',command=savefilepath).place(x=450,y=48)

tk.Label(win,text='重命名文件，默认1-2-3-').place(x=0,y=150)
tk.Button(win,text='重命名文件',command=renames).place(x=300,y=150)

tk.Label(win,text='合并选定的文件夹里所有的音频文件，格式必须一样').place(x=0,y=200)
tk.Button(win,text='合并音频视频文件',command=merge).place(x=300,y=200)

file_type=tk.StringVar()
tk.Label(win,text='输入要转换出的文件格式,比如mp3 mp4').place(x=0,y=250)
tk.Entry(win,width=10,textvariable=file_type).place(x=220,y=250)
tk.Button(win,text='转换',command=conversionfile).place(x=300,y=250)
tk.Button(win,text='批量转换',command=conversionfiles).place(x=350,y=250)



win.mainloop()