from typing import Union
from fastapi import FastAPI
from service import service
import dpkt
import json


app = FastAPI()


@app.get("/")
def getLocation():
    with open('data/trabalho1.pcapng', 'rb') as f:
        pcap = dpkt.pcapng.Reader(f)
        return service.getLocation(pcap)
        
