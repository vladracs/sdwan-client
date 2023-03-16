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
![Screenshot 2023-03-16 at 10 18 51](https://user-images.githubusercontent.com/76786046/225572100-2e42582d-5f5d-45ba-8041-2526483cd533.png)


WESTEU
![sdwc westeu](https://user-images.githubusercontent.com/76786046/225564392-5bc22166-703d-4ebb-bcdb-b17881fda76d.png)

All linux instance have sdwc installed and a nginx webserver.
  sdwc must be activated via token collected during node creation in the portal/API 
sdwc must be downloaded on the Windows VM and user must manually authenticate
