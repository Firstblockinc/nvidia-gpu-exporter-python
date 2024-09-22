from pysnmp.hlapi.v1arch import *
from pysnmp.hlapi.v3arch import *

def get_snmp_data(oid, target):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),  # Community string
               UdpTransportTarget((target, 161)),   # Target GPU machine IP
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    if errorIndication:
        print(f"Error: {errorIndication}")
        return None
    elif errorStatus:
        print(f"Error: {errorStatus.prettyPrint()}")
        return None
    else:
        for varBind in varBinds:
            return varBind.prettyPrint().split('=')[-1].strip()
