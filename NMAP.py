import nmap #importing the nmap module
#import pythonnmap
class NMAP:
  def NmapScan(self, url):#declaring a function
    nm=nmap.PortScanner()
    nm.scan(url)#scanning the url
    for host in nm.all_hosts():#for all hosts
      for proto in nm[host].all_protocols():
        lport=nm[host][proto].keys()#getting all the keys
        #lport.sort()
        dictionary=dict()
        openport=[]
        filteredport=[]
        for port in lport :
          dictionary[port]=nm[host][proto][port]['state'] #creating a dictionary
          #print(dictionary)
          for portkey,portvalue in dictionary.items():
            if(portvalue=='open'):
              openport.append(portkey)
            if(portvalue=='closed'):
              filteredport.append(portkey)
      #print('OpenPort:- ', openport)
      #print('ClosedPort:-',filteredport)
      return len(openport)/100
                          
#url=str(input('URl:-'))
#NmapScan(url)

