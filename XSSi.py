import requests
import time
import sys
class XSS:
  def XSSInjection(self, url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
    pog = 'g'
    #print (pog)
    lineexe=0
    queryexe=0
    if pog == "g" :
      try:
        site=url
        #site = input("URL : ")
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
        payload = open("xss.txt", "r")
      except FileNotFoundError:
        print()
        print("The file doesn't exists, try again !")
        sys.exit(0)
      print()
      print("Test in progress... \n")
      time.sleep(1)
      f = open("xss.txt","r")
      l = 1
      for line in f:
        lineexe=lineexe+1
        print()
        print("Testing payload " + str(line))
        if line in requests.get(site + line, headers=header).text:
          queryexe=queryexe+1
          print("XSS FOUND HERE : \n"+ line)
          print(requests.get(site + line, headers=header).url)
        else:
          print(" The payload" + str(line) + "does not trigger the XSS Filter." )
          print()
          l == 1
      print(queryexe/lineexe)
    else:
      print("unknown answer ")
      sys.exit(0)
