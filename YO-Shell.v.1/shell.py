<This is the bash command simulator written in python and when entered input such as bash commands give the output exactly as the bash terminal.> 

import os,stat,sys
import time,subprocess,shutil


class historyManager(object):
    def __init__(self):
        self.command_history = []
		
    def push_command(self,cmd):
        self.command_history.append(cmd)
		
    def get_commands(self):
        return self.command_history
		
    def number_commands(self):
        return len(self.command_history)
		
class parserManager(object):
    def __init__(self):
        self.parts = []
        
    def parse(self,cmd):
        self.parts = cmd.split(" ")
        return self.parts
		
class commandManager(parserManager,historyManager):
    def __init__(self):
        self.command = None
		
    def run_command(self,cmd):
        self.command = cmd
        self.command = self.parse(self.command)
        return self.command
       
    def lsfun(self):
        path=os.getcwd()
        files = []
        files=os.listdir(path)
        #for name in os.listdir(path):
           # if os.path.isfile(os.path.join(path,name)):
             #   files.append(name)
        return files
        
		
    def ls(self,parts):
        try:
            if(parts[0]=='ls' and parts[1]=='-l'):
                files=[]
                files=self.lsfun()       
                print(" File Name         Size       Permissions       Accessed Time                  Modified Time                        changed time")
                print("-----------        -----      ------------      --------------                 --------------                       ------------")
                for x in range(0,len(files)):
                    print(files[x],'\t\t  ',(os.stat(files[x]).st_size),'\t\t',(oct(os.stat(files[x])[stat.ST_MODE])[-3:]),'\t\t',(time.ctime(os.path.getmtime(files[x]))),'\t',(time.ctime(os.stat(files[x]).st_atime)),'\t',(time.ctime(os.stat(files[x]).st_ctime)))
                #print(os.stat(files[x]).st_size) #size
                #print(oct(os.stat(files[x])[stat.ST_MODE])[-3:]) #permissions
                #print(time.ctime(os.path.getmtime(files[x])) #modified time
                #print(time.ctime(os.stat(files[x]).st_atime)) #accessed time
                #print(time.ctime(os.stat(files[x]).st_ctime))
            elif(parts[0]=='ls' and parts[1]=='-a'):
                files=[]
                path=os.getcwd()
                atime = lambda f: os.stat(os.path.join(path, f)).st_atime
                files= list(sorted(os.listdir(path), key=atime))
                print(" File Name         Size       Permissions       Accessed Time                        Modified Time                  changed time")
                print("-----------        -----      ------------      --------------                       --------------                 ------------")
                for x in range(0,len(files)):
                   print(files[x],'\t\t  ',(os.stat(files[x]).st_size),'\t\t',(oct(os.stat(files[x])[stat.ST_MODE])[-3:]),'\t\t',(time.ctime(os.path.getmtime(files[x]))),'\t',(time.ctime(os.stat(files[x]).st_atime)),'\t',(time.ctime(os.stat(files[x]).st_ctime)))
            elif(parts[0]=='ls' and parts[1]=='-m'):
                files=[]
                path=os.getcwd()
                mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
                files= list(sorted(os.listdir(path), key=mtime))
                print(" File Name         Size       Permissions       Accessed Time                        Modified Time                  changed time")
                print("-----------        -----      ------------      --------------                       --------------                 ------------")
                for x in range(0,len(files)):
                    print(files[x],'\t\t  ',(os.stat(files[x]).st_size),'\t\t',(oct(os.stat(files[x])[stat.ST_MODE])[-3:]),'\t\t',(time.ctime(os.path.getmtime(files[x]))),'\t',(time.ctime(os.stat(files[x]).st_atime)),'\t',(time.ctime(os.stat(files[x]).st_ctime)))   
            elif(parts[0]=='ls' and parts[1]=='-c'):
                files=[]
                path=os.getcwd()
                ctime = lambda f: os.stat(os.path.join(path, f)).st_ctime
                files= list(sorted(os.listdir(path), key=ctime))
                print(" File Name         Size       Permissions       Accessed Time                        Modified Time                  changed time")
                print("-----------        -----      ------------      --------------                       --------------                 ------------")
                for x in range(0,len(files)):
                    print(files[x],'\t\t  ',(os.stat(files[x]).st_size),'\t\t',(oct(os.stat(files[x])[stat.ST_MODE])[-3:]),'\t\t',(time.ctime(os.path.getmtime(files[x]))),'\t',(time.ctime(os.stat(files[x]).st_atime)),'\t',(time.ctime(os.stat(files[x]).st_ctime)))               
            else:
                print("command not found")
        except IndexError:
            self.lsmain()

    def lsmain(self):
        print("File Listing")
        print("------------")
        
        for f in self.lsfun():
            print(f)
        print("------------")


			
    def cat(self,file):
        f = open(file,'r')
        print(f.read())
		
			
    def cd(self,dir):
        k=os.path.join(os.getcwd(),dir)
        if(os.path.isdir(k)):
            os.chdir(k)       
        else:
            print("Specified directory doesn't exist")
            
    def cp(self,file1,file2):
        if(os.path.isfile(file2)):
            shutil.copyfile(file1, file2)
            print("copy successful")
        else:
            file = open('file2','w+')
            shutil.copyfile(file1, file2)
            print("copy successful")
		

	
    def mv(self,file1,file2):
        os.rename(file1,file2)
        print("file has been renamed")
	 	
    def rm(self,file):
        os.remove(file)
        
    def chmod(self,parts):
        subprocess.call(['chmod',parts[1], parts[2]])
	
    def wc(self,parts):
        if(parts[0]=="wc" and parts[1]=="-l"):
            if(os.path.isfile(parts[2])):
                self.linecount =0
                with open(parts[2], 'r') as f:
                    for line in f:
                        self.linecount += 1
                print("line count = %d"%(self.linecount))

        elif (parts[0]=="wc" and os.path.isfile(parts[1])):
            self.linecount = 0
            self.wordcount = 0
            self.charcount = 0
            with open(parts[1],'r') as f:
                for line in f:
                    self.words = line.split()
                    self.linecount += 1
                    self.wordcount += len(self.words)
                    self.charcount += len(line)
            print("line count= %d, word count= %d, charcount= %d"%(self.linecount,self.wordcount,self.charcount))
        else:
            print("command not found")

class driver(object):
    def __init__(self):
        self.history = historyManager()
        self.commands = commandManager()
        self.number_commands = 0
    def runShell(self):
        number_commands = 0
        while True:
            self.input = input("parser-$ ")         # get command
            self.history.push_command(self.input)   # put in history
            parts = self.commands.run_command(self.input)
            if(parts[0]=='wc'):
                self.commands.wc(parts)
            elif(parts[0]=='cat'):
                self.commands.cat(parts[1])
            elif(parts[0]=='cd' and parts[1]=='..'):
                os.chdir("..")
            elif(parts[0]=='cd' and parts[1]=='~'):
                os.chdir((os.path.expanduser('~')))
            elif(parts[0]=='cd'):
                self.commands.cd(parts[1])
   
            elif(parts[0]=='cp'):
                self.commands.cp(parts[1],parts[2])
            elif(parts[0]=='history'):
                hi=[]
                hi=self.history.get_commands()
                for x in range(0,self.history.number_commands()): 
                    print("%d %s"%(x+1,hi[x]))
            elif(parts[0]=='mv'):
                self.commands.mv(parts[1],parts[2])
            elif(parts[0]=='rm'):
                self.commands.rm(parts[1])
            elif(parts[0]=='ls'):
                self.commands.ls(parts)
            elif(parts[0]=='chmod'):
                self.commands.chmod(parts)
            else:
                print("command not found")


            #print(parts)
if __name__=="__main__":
    d = driver()    
    d.runShell()
