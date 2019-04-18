#!/usr/bin/env python

from lib.HostsHandler   import *
from lib.PingHandler    import *

if __name__ == '__main__':
    #Initialize a host handler
    hh = HostsHandler()
    #Get hosts from "hosts" file
    hh.getHostsFromFile()
    #Print a formatted version of the hosts list
    #hh.printHostsList()
    #Initialize a ping handler using the hosts list from the host handler 
    ph = PingHandler( hh.getHostsList() )
    #Pings all hosts in list
    ph.pingHosts()
    #Print connection status results for each host in list
    ph.printPingResults()


