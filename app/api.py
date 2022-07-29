from csv import DictWriter
import json
from unittest import async_case
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import sys
from pybp.pederson import PedersonCommitment
from pybp.rangeproof import RangeProof
from fastapi.responses import  FileResponse
import pickle
import zipfile
import os
import time
import asyncio

app = FastAPI()  

origins = [
    "http://localhost:3000",  
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Varg = " "

@app.post("/commitment")
async def check_bids(val:dict) -> dict: 
    value = int(val['value'])
    rp = RangeProof(32) 
    proofval = value & (2**32 - 1)
    rp.generate_proof(proofval)
    global Varg
    Varg = PedersonCommitment(value, b = rp.gamma)
    final_val = Varg.get_commitment()
    return {'bid_x':final_val[0], 'bid_y':final_val[1]}
           
    

@app.get("/opening") 
async def get_vals() -> dict: 
    return {'h_x':Varg.h[0], 'h_y':Varg.h[1], 'r':Varg.b, 'v': Varg.v}