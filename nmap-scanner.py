import nmap # pip3 install python-nmap
import sys

target = str(sys.argv[1])
ports = [21,22,80,139,443,8080]

scan_v = nmap.PortScanner()

print("\nScanning target" + target + " for ports 21, 22,80, 139, 443, 8080...\n")

for port in ports:
    portscan = scan_v.scan(target, str(port))
    print("Port ", port, " is ", portscan['scan'][target]['tcp'][port]['state'])

print("\nHost ", target,  portscan['scan'][target]['status']['state'])