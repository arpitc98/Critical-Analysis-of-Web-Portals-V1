from NMAP import *
from SQLi import *
from XSSi import *
from Default import *
from Report import *

class Controller:
  def malicious(self,sql,xss,nmap,dup,url):
    sqlscore=0
    xssscore=0
    nmapscore=0
    dupscore=0
    #print("Controller")
    if(sql == 1):
      sqlscore=0
      sqlobj= SQLAutomation()
      sqlscore=sqlobj.SQLInjection(url)
    if(xss==1):
      xssscore=0
      xssobj=XSS()
      #print("Xsss")
      xssobj.XSSInjection(url)
    if(nmap==1):
      nmapscore=0
      print("NMAP")      
      nmobj= NMAP()
      nmapscore=nmobj.NmapScan(url)
    if(dup==1):
      dupscore=0
      defaultobj=Default(url)
      defaultobj.timePass(1)
      #forms=defaultobj.usernamePassword(url)
      #defaultobj.find(forms,url)
      #usernamepassword(url)
    reportobj= Report()
    reportobj.generateReport(sqlscore,xssscore,nmapscore,dupscore)
