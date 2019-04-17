#Library to handle hosts listed in file "hosts" for pyPing application
import os
from prettytable import PrettyTable

#Single Element Of HostsList
class HostElement:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip       = ip

    def __str__(self):
        msg = self.hostname + '\t\t\t\t' + self.ip + '\n'
        return msg

#Handles the list of hosts read from "hosts"
class HostsHandler:

    def __init__(self):
        #Initializer
        self.HostsList = []

    def __len__(self):
        #Get number of hosts
        return len(self.HostsList)
    
    def __str__(self):
        #Return hosts list for printing
        msg = ''
        msg += "\nHosts List:\n"
        for i in range(0 , len(self)):
            msg += str(self.HostsList[i])
        return msg
    
    #Gets the "hosts" file path inside the package
    def getHostsFilePath(self):
        filePath = str(os.getcwd()) + "/hosts"
        return filePath

    #Reads the list of hosts from file and store it in self.HostsList
    def getHosts(self):
        #Gets filepath
        filePath = self.getHostsFilePath()
        #Opens file
        FILE = open(filePath, "r")
        #Reads first line in hosts file
        dataLine = FILE.readline()
        #Reads line by line untill and stores it in HostsList (hostname & ip)
        while not dataLine is None and not len(dataLine) == 0:
            #Splits data by hostname and ip
            hostname, ip = dataLine.split()
            #Creates HostElement ( [hostname, ip] pair ) and appends to list 
            self.HostsList.append( HostElement(hostname,ip) )
            dataLine = FILE.readline()

    #Special method to print a formatted table of HostsList using PrettyTable external library
    def printHostsList(self):
        t = PrettyTable(['Hostname', 'IP'])
        for i in range(0 , len(self)):
            t.add_row([self.HostsList[i].hostname, self.HostsList[i].ip])
        print t
