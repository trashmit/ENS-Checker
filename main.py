import requests, os, time
from concurrent.futures import ThreadPoolExecutor
from web3 import Web3
from ens import ENS

w3= Web3()
available = []

"""
ENS Requirements:
Under 3 characters 
"""

#put infura connection here 
URL ="https://mainnet.infura.io/v3/?????????????????????"

if not os.path.exists('available.txt'):
        input("available.txt does not exist in current folder. Please restart when it exists.")

if not os.path.exists('list.txt'):
        input("list.txt does not exist in current folder. Please restart when it exists.")

with open("list.txt", "r") as f:
    raw_usernames = f.read().splitlines() 

usernames = []
for username in raw_usernames:
    if len(username) > 2:
        usernames.append([username, ENS.namehash(f"{username}.eth").hex().replace('0x', '0x02571be3')])

totalusernames = len(usernames) 
print(f"{totalusernames} usernames loaded.")

def get(username):
        params = {
            "jsonrpc": "2.0",
            "method": "eth_call",
            "params": [
                {
                "to": "0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e",
                "data": username[1]
                },
                "latest"
            ],
        "id": 3      
        }
        data = requests.post(URL, json=params).json()
        #IF USERNAME IS AVAILABLE!

        if data["result"]=="0x0000000000000000000000000000000000000000000000000000000000000000":
            #print(username[0], "NOT TAKEN")
            available.append(username[0])
        #IF USERNAME IS NOT AVAILABLE!

        #else:
            #print(username[0], "TAKEN")

def main():
    t1 = time.time()
    with ThreadPoolExecutor(max_workers=200) as pool:
        pool.map(get, usernames)
    print(f"Finished in {time.time()-t1} seconds")
    with open("available.txt", "a") as f:
        for item in available:
            f.write(item + "\n")
    print(f"Found {len(available)} ens names stored in available.txt")
                     
main()