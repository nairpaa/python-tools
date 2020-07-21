# https://en.wikipedia.org/wiki/IEEE_802.11#Management_frames
from scapy.all import *

iface = "wlp2s0"

def h_packet(packet):
    if packet.haslayer(Dot11ProbeReq) or packet.hashlayer(Dot11ProbeResp) or pakcet.hashlayer(Dot11AssoReq):
        print("SSID identified " + print.info)

os.system("iwconfig" + iface + "mode monitor")

print("sniffing traffic on interface " + iface)
sniff(iface=iface, prn=h_packet)
