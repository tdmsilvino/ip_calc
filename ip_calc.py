"""ip_calc.py  Copyright (C) 2022 Thiago Silvino
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions;
"""
from ipaddress import IPv4Interface

def show_address_info(addr_info: dict):
    """ Receives a dictionary with subnet information and prints it """
    for k, v in addr_info.items():
        print(f'{k}:\t{v}')

def address_info(addr: str) -> dict:
    """Receives a string with IP address in on of these forms:
        '10.123.4.5/24'
        '10.123.4.5/255.255.128.0'
        '10.123.4.5 255.255.128.0'
        '10.123.4.5 0.0.63.255'
       Returns a dictionary with subnet information.
    """
    try:
        ipaddr = IPv4Interface(addr)
        prefixlen = ipaddr.network.prefixlen
        if prefixlen == 32:
            host_min = ipaddr.ip
            host_max = ipaddr.ip
            host_net = '1'
        elif prefixlen == 31:
            host_min = ipaddr.network[0]
            host_max = ipaddr.network[1]
            host_net = '2'
        else:
            host_min = ipaddr.network[1]
            host_max = ipaddr.network[-2]
            host_net = ipaddr.network.num_addresses - 2
        addr_info = dict(Address=ipaddr.ip,
                        Netmask=f'{ipaddr.netmask} = {prefixlen}',
                        Wildcard=ipaddr.hostmask,
                        Network=ipaddr.network,
                        HostMin=host_min,
                        HostMax=host_max,
                        Broadcast=ipaddr.network.broadcast_address,
                        HostsNet=host_net)
        return addr_info
    
    except ValueError:
        print(f'{addr} is not a valid value')

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        show_address_info(address_info(f'{sys.argv[1]}/{sys.argv[2]}'))
    elif len(sys.argv) == 2:
         show_address_info(address_info(f'{sys.argv[1]}'))
    else:
        print("""Examples of usage:
                ipycalc.py 10.123.4.5/24
                ipycalc.py 10.123.4.5/255.255.128.0
                ipycalc.py 10.123.4.5 255.255.128.0
                ipycalc.py 10.123.4.5 0.0.63.255
                """)
