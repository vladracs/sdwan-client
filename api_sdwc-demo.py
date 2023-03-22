# Disclaimer: Not to be considered as best practices in using VMware VCO API Meant to be used in Lab environments 
# Please test it and use at your own risk
# Please note that VMWare API and Support team - do not guarantee this samples It is provided - AS IS - i.e. while we are glad to answer questions about API usage and behavior generally speaking, VMware cannot and do not specifically support these scripts

#Sample API script that leverage the Vmware SDWAN Client Portal API to build a demo setup

#It builds groups (users, server, connector), nodes (users, server, connectors), and network (with rules and context)
# Disclaimer: Not to be considered as best practices in using VMware VCO API Meant to be used in Lab environments 
# Please test it and use at your own risk
# Please note that VMWare API and Support team - do not guarantee this samples It is provided - AS IS - i.e. while we are glad to answer questions about API usage and behavior generally speaking, VMware cannot and do not specifically support these scripts

# author: vfrancadesou@vmware.com

import json
import requests
import os

myapitoken = "%s" %(os.environ['API_TOKEN'])
myemail = "vfrancadesou@vmware.com"
useremail = "vfrancadesou+user1@vmware.com"
mydomain = "myacme.com"

base_url = "https://api.ananda.net"
headers = {
    "accept": "application/json;charset=UTF-8",
    "Authorization": myapitoken,
}

s = requests.Session()
s.headers.update(headers)
auth = s.post(f"{base_url}/login-accounts/v1.1/auths/apis/oauth/token")
token_type = json.loads(auth.content)["token_type"]
access_token = json.loads(auth.content)["access_token"]

auth_headers = {
    "authorization": f"{token_type} {access_token}"
}

s.headers.update(auth_headers)
orgId = json.loads(auth.content)["meta"]["orgId"]
print("ORG ID="+orgId)
#Creating Groups
# ananda API fails if you try to repost an existing object. so must always check for existence
get_group_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/groups"
groups = s.get(get_group_url, json="")
groups = json.loads(groups.content)
addgroup=True
for group in groups:
    if group["name"]=="user-group":
        user_group_id=group["groupId"]
        #print(user_group_id)
        addgroup=False
if (addgroup):
    group_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/groups"
    group_data = {
        "name": "user-group",
        "desc": "users",
        "status": "active",
        "new": True
    }
    group = s.post(group_url, json=group_data)
    user_group_id = json.loads(group.content)["groupId"]
    

#GROUP Servers
addgroup=True
for group in groups:
    if group['name']=="server1-group":
        server1_group_id = group["groupId"]
        addgroup=False
if (addgroup):
    group_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/groups"
    group_data = {
        "name": "server1-group",
        "desc": "server 1",
        "status": "active",
        "new": True
    }
    group = s.post(group_url, json=group_data)
    #print(group)
    server1_group_id = json.loads(group.content)["groupId"]

addgroup=True
for group in groups:
    if group['name']=="server2-group":
        server2_group_id = group["groupId"]
        addgroup=False
if (addgroup):
    group_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/groups"
    group_data = {
    "name": "server2-group",
    "desc": "server 2",
    "status": "active",
    "new": True
}
    group = s.post(group_url, json=group_data)
    server2_group_id = json.loads(group.content)["groupId"]

addgroup=True
for group in groups:
    if group['name']=="servers-group":
        servers_group_id = group["groupId"]
        addgroup=False
if (addgroup):
    group_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/groups"
    group_data = {
    "name": "servers-group",
    "desc": "All servers",
    "status": "active",
    "new": True
}
    group = s.post(group_url, json=group_data)
    servers_group_id = json.loads(group.content)["groupId"]

get_group_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/groups"
groups = s.get(get_group_url, json="")
groups = json.loads(groups.content)
#GROUP Client Connectors
addgroup=True
for group in groups:
    if group['name']=="cc1-group":
        cc1_group_id = group["groupId"]
        addgroup=False
if (addgroup):
    group_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/groups"
    group_data = {
    "name": "cc1-group",
    "desc": "cc 1",
    "status": "active",
    "new": True
}
    group = s.post(group_url, json=group_data)
    cc1_group_id = json.loads(group.content)["groupId"]

addgroup=True
for group in groups:
    if group['name']=="cc2-group":
        cc2_group_id = group["groupId"]
        addgroup=False
if (addgroup):
    group_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/groups"
    group_data = {
    "name": "cc2-group",
    "desc": "cc 2",
    "status": "active",
    "new": True
}
    group = s.post(group_url, json=group_data)
    cc2_group_id = json.loads(group.content)["groupId"]
######

#Creating NODES
#find own user id , used during invites
if(True):
    get_user_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/users"
    users = s.get(get_user_url, json="")
    myusers = json.loads(users.content)

    for users in myusers:
        if( users['email']==myemail):
                myuser_id = users['userId']
                print(users['email']," ", myuser_id)
    user_url = f"{base_url}/register-accounts/v1.1/idps/api/orgs/{orgId}/invs/roles/standard/emails/{useremail}"
    user_data = {"email":useremail,"firstName":useremail,"groupIds":[user_group_id],
    "inviteId":"string","invitedBy":myuser_id,"lastName":"null","regType":"register","roleType":"STANDARD","type":"USER"}
    user = s.post(user_url, json=user_data)
    for users in myusers:
        if( users['email']==useremail):
                user_id = users['userId']

#Creating NODES - SERVERS
get_servers_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/servers"
servers = s.get(get_servers_url, json="")
servers = json.loads(servers.content)
addserver=True
for server in servers:
    if server['name']=="server1":
        server1_id =server["userId"]
        addserver=False
if (addserver):
    #{"name":"serv1","desc":null,"groupIds":["641af10a1733df7c7ab368e5","641af1cd85764412d3d00b03"],"serverHostname":"srv1","subdomain":"acme.com"}
    server_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/servers"
    server_data = {
        "name": "server1",
        "desc": "server1",
        "groupIds": [
            server1_group_id,servers_group_id
        ],
        "serverHostname": "srv1",
        "subdomain": mydomain
    }
    server1 = s.post(server_url, json=server_data)
    server1_token = json.loads(server1.content)["token"]
    print("server 1 token=",server1_token)
    for server in servers:
        if server['name']=="server1":
         server1_id =server["userId"]

addserver=True

for server in servers:
   
    if server['name']=="server2":
        server2_id =server["userId"]
        addserver=False
if (addserver):
    server_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/servers"
    server_data = {
    "name": "server2",
    "desc": "server2",
    "groupIds": [
        server2_group_id,servers_group_id
    ],
    "serverHostname": "srv2",
    "subdomain": mydomain
}
    server2 = s.post(server_url, json=server_data)
    server2_token = json.loads(server2.content)["token"]
    print("server 2 token=",server2_token)
    for server in servers:
        if server['name']=="server2":
         server2_id =server["userId"]
#Creating CLIENT CONNECTOR NODE
get_gw_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/gateways"
gws = s.get(get_gw_url, json="")
gws = json.loads(gws.content)
addgw=True
for gw in gws:
    
    if gw['name']=="cc1":
        gw1_id=gw["userId"]
        addgw=False
if (addgw):
    gw_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/gateways"
    gw_data = {
        "name": "cc1",
        "interfaceName": "eth0",
        "desc": "my cc1",
        "gatewayIps": [
            {
                "from": "10.2.0.65",
                "to": "10.2.0.75"
            }
        ],
        "groupIds": [
            cc1_group_id

        ],
        "dnsHosts": [
            {
                "hostname": "myacme.com",
                "tunnel": True
            }
        ]
    }
    gw = s.post(gw_url, json=gw_data)
    gw_token = json.loads(gw.content)["token"]
    print("cc token=",gw_token)
    for gw in gws:
        if gw['name']=="cc":
            gw1_id=gw["userId"]

# BUILDING RULES
get_rules_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/rules"
rules = s.get(get_rules_url, json="")
rules = json.loads(rules.content)
addrule=True
for rule in rules:
    if rule['name']=="rule1":
        rule1_id = rule["ruleId"]
        addrule=False
if (addrule):
    rule_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/rules"
    rule_data = {"name":"rule1","description":"web,ping","status":"active","allowType":"ALLOW","new":True,"predefinedNetworkServices":["HTTP","ICMP"]}
    rule = s.post(rule_url, json=rule_data)
    rule1_id = json.loads(rule.content)["ruleId"]

addrule=True
for rule in rules:
    if rule['name']=="rule2":
        rule2_id = rule["ruleId"]
        addrule=False
if (addrule):
    rule_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/rules"
    rule_data = {"name":"rule2","description":"web,ping,ssh","status":"active","allowType":"ALLOW","new":True,"predefinedNetworkServices":["HTTP","ICMP","SSH"]}
    rule = s.post(rule_url, json=rule_data)
    rule2_id = json.loads(rule.content)["ruleId"]

### DELETE CONTEXT
#context_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/contexts/640dc4fe6f1d8c16d340b054"
#context = s.delete(context_url, json="")
#print(context)

# BUILDING CONTEXT

get_contx_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/contexts"
contxs = s.get(get_contx_url, json="")
contxs = json.loads(contxs.content)
addcontx=True
for contx in contxs:
    
    if contx['name']=="contx-linux":
        context1_id = contx["contextId"]
        addcontx=False
if (addcontx):
    
    context_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/contexts"
    context_data = {
        "name": "contx-linux",
        "description": "The description of my new context",
        "times": [
            {
                "start": {
                    "dateTime": None,
                    "tz": "Europe/Berlin"
                },
                "end": {
                    "dateTime": None,
                    "tz": "Europe/Berlin"
                },
                "recurrence": {
                    "cycle": {
                        "type": "WEEKDAYS",
                        "weekDays": [],
                        "period": 1
                    }
                }
            }
        ],
        "status": "active",
        "allowType": "ALLOW",
        "new": True,
        "osTypes": [
            "LINUX"
        ],
        "locations": [],
        "hasAntivirus": False,
        "hasScreenSaver": False
    }
    context = s.post(context_url, json=context_data)
    context1_id = json.loads(context.content)["contextId"]

addcontx=True
for contx in contxs:
    
    if contx['name']=="contx-windows":
        context2_id = contx["contextId"]
        addcontx=False
if (addcontx):
    
    context_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/contexts"
    context_data = {
        "name": "contx-windows",
        "description": "The description of my new context",
        "times": [
            {
                "start": {
                    "dateTime": None,
                    "tz": "Europe/Berlin"
                },
                "end": {
                    "dateTime": None,
                    "tz": "Europe/Berlin"
                },
                "recurrence": {
                    "cycle": {
                        "type": "WEEKDAYS",
                        "weekDays": [],
                        "period": 1
                    }
                }
            }
        ],
        "status": "active",
        "allowType": "ALLOW",
        "new": True,
        "osTypes": [
            "WIN"
        ],
        "locations": [],
        "hasAntivirus": False,
        "hasScreenSaver": False
    }
    context = s.post(context_url, json=context_data)
    context2_id = json.loads(context.content)["contextId"]

#BUILDING NETWORKS


# ananda API fails if you try to repost an existing object. so must always check for existence
get_net_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/v2lans"
nets = s.get(get_net_url, json="")
nets = json.loads(nets.content)

addnet=True
for net in nets:
    if net['name']=="segment1-HS":
        #print("found net")
        addnet=False
if (addnet):
    network_url = f"{base_url}/manage-accounts/v1.1/api/orgs/{orgId}/v2lans"
    network_hub_data = {"name":"segment1-HS","topology":{"type":"HUB",
                                                   "sourceNobs":[{"id":user_group_id,"type":"group"}],
                                                   "targetNobs":[{"id":server1_group_id,"type":"group"},{"id":cc1_group_id,"type":"group"}]},
                                                   "new":True,
                                                   "isKeepConnected":False,
                                                   "policy":{"ruleIds":[rule1_id],
                                                   "sourceContextId":context2_id}}
    network = s.post(network_url, json=network_hub_data)

addnet=True
for net in nets:
    if net['name']=="segment2-mesh":
        addnet=False
if (addnet):
    network_mesh_data ={
        "name": "segment2-mesh",
        "topology": {
            "type": "MESH",
            "sourceNobs": [
                {
                    "id": servers_group_id,
                    "type": "group"
                }
            ]
        },
        "new": True,
        "isKeepConnected": False,
        "policy": {
            "ruleIds": [
                rule2_id
            ],
            "sourceContextId": context1_id
        }
    }

    network = s.post(network_url, json=network_mesh_data)

addnet=True
for net in nets:
    if net['name']=="segment3-HS":
        addnet=False
if (addnet):
    network_mesh_data ={
        "name": "segment2-HS",
        "topology": {
            "type": "HUB",
            "sourceNobs": [
                {
                    "id": user_group_id,
                    "type": "group"
                },
                {
                    "id": server2_group_id,
                    "type": "group"
                }
            ]
        },
        "new": True,
        "isKeepConnected": False,
        "policy": {
            "ruleIds": [
                rule1_id
            ],
            "sourceContextId": context1_id
        }
    }

    network = s.post(network_url, json=network_mesh_data)
