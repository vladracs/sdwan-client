# sdwan-client

Scripts to build a VMware SD-WAN Client LAB/Demo

Example of usage: (these tokens are needed to active the corresponding nodes:

vfrancadesou% python3 api_sdwc.py

ORG ID=63d2641f61bfe

server 1 token = bm(...)MWJmZ2MTVub

server 2 token = bml(...)WQ1bmF2YTV

cc token       = bml(...)odjc2YjBmO

AZ CLI LAB builds resources in 2 region:

WESTUS
![sdwc westus](https://user-images.githubusercontent.com/76786046/225563568-f7e89537-aaa9-4ef0-8b4e-13cddeef0a64.png)

WESTEU
![sdwc westeu](https://user-images.githubusercontent.com/76786046/225564392-5bc22166-703d-4ebb-bcdb-b17881fda76d.png)

All linux instance have sdwc installed and a nginx webserver.
  sdwc must be activated via token collected during node creation in the portal/API 
sdwc must be downloaded on the Windows VM and user must manually authenticate
