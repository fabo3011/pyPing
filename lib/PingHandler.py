#Library to handle connection tests using ping to a given list of hosts for pyPing application
import os
import subprocess
import time
from prettytable import PrettyTable

class PingHandler:

    def __init__(self, HostsList):
        #Initializer
        self.HostsList = HostsList
        self.PingResultsList = []
        #Resize Ping Results List based on Hosts List length
        for i in range(0,len(self.HostsList)):
            self.PingResultsList.append('N/A')
    
    def __len__(self):
        #Get number of hosts
        return len(self.HostsList)

    #Pings specified IP
    def pingIP(self, IP):
        #Execute print command
        ping = subprocess.Popen(['ping', '-c', '1', IP],
                    stdout = subprocess.PIPE,
                    stderr = subprocess.STDOUT)
        return ping
    
    #Gets connection status from output obtained after the ping porcess has run.
    #Ping successful    -> status = OK
    #Ping unsuccessful  -> status = LOST
    def getConnectionStatusFromStdout(self, stdout):
        try:
            #Split stdout to get the individual lines
            stdoutLines         = stdout.split('\n')
            #Use line 4 to determine if ping was successful
            stdoutStatistics     = stdoutLines[4].split(',') 
            #Use previous to last argument in stdout statistics corresponding to packet loss
            #if packets lost = 100% -> status = OK
            #if packets lost = 0%   -> status = LOST 
            stdoutStatisticsArgs = stdoutStatistics[len(stdoutStatistics)-2].split()
            stdoutPacketLoss     = stdoutStatisticsArgs[0]
            if stdoutPacketLoss == '0%':
                return 'OK'
            else:
                return 'LOST'
        except:
            #if ping stdout cant be processed, status = N/A (Not Available)
            return 'N/A'

    #Pings all hosts in list
    def pingHosts(self):
        #Stores results from each ping executed
        pingSubprocessList = []
        #Ping each host
        for i in range(0,len(self.HostsList)):
            ping = self.pingIP(self.HostsList[i].ip)
            pingSubprocessList.append(ping)

        for i in range(0,len(pingSubprocessList)):
            #Get ping execution output
            stdout, stderr = pingSubprocessList[i].communicate()
            #Determines status based on ping stdout
            status = self.getConnectionStatusFromStdout(stdout)
            #Store connection status in Ping Results List
            self.PingResultsList[i] = status

    #Uses PrettyTable External library to print a table of results in terminal of the status connection of each
    #host in the list
    def printPingResults(self):
        t = PrettyTable(['Hostname', 'IP', 'Status'])
        for i in range(0 , len(self)):
            t.add_row([self.HostsList[i].hostname, self.HostsList[i].ip, self.PingResultsList[i]])
        print t