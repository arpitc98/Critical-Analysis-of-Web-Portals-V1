import requests
import time
import sys
#print("SQLI")

class SQLAutomation:
  def SQLInjection(self, url):
    queryexe=0
    linecount=0
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
    pog = 'g'
    print (pog)
    if pog == "g" :
      try:
        site = url#input("URL : ")
        r = requests.post(site, headers=header)
        time.sleep(1)
        print()
        print("The site respond !" )
      except:
        print()
        print('does the script respond...')
        time.sleep(3)
        print()
        print("The Site doesn't respond, try again. (with https:// or http:// ...)")
        sys.exit(0)
        print()
      try:
        payload = open("SQL.txt", "r")
      except FileNotFoundError:
        print()
        print("The file" + payload + "doesn't exists, try again !")
        sys.exit(0)
      print()
      print("Test in progress... \n")
      time.sleep(1)
      f = open("SQL.txt","r")
      l = 1
      for line in f:
        linecount=linecount+1
        if line in requests.get(site + line, headers=header).text:
          linecount=linecount
          #print("Not Vulnerable to:" + line)
          #print(requests.get(site + line, headers=header).url)
        else:
          queryexe=queryexe+1
          print("Vulnerable to: "+line)
      else:
        print("unknown answer ")
    returnvalue=queryexe/linecount
    return(returnvalue)
