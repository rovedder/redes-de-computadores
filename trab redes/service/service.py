import dpkt
from dpkt.utils import inet_to_str
import requests
import json


def getLocation(pcap):
    # For each packet in the pcap process the contents
    ips = []
    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)

        if not isinstance(eth.data, dpkt.ip.IP):
            continue

        ip = eth.data
        ip_address = inet_to_str(ip.dst)
        
        ips.append(ip_address)

    ips = list(set(ips))
    locations = []
    for ip in ips:
        request_url = 'https://ipinfo.io/' + ip + '/json'
        response = requests.get(request_url)
        result = response.content.decode()
        result  = json.loads(result)
        if "loc" in result:
           locations.append(result)

    return locations