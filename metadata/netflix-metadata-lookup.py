""" 
Taken from Steffie Jacob Eravuchira, Vaibhav Bajpai, Juergen Schoenwaelder,
https://github.com/vbajpai/ripe69-python3-toolset/blob/master/ripe69-python3-toolset.ipynb

Modified print statements to work with Python 2.7 and to perform required lookups
"""

import sys
import requests
import json

import sqlite3
import pandas as pd

import codecs
import numpy as np

DB_PATH = '../data/netflix-data.db'

def get_json_resource_from_absolute_uri(url, query_params):
    try: res = requests.get(url, params = query_params)
    except Exception as e: print >> sys.stderr, e
    else:
        try: res_json = res.json()
        except Exception as e: print >> sys.stderr, e
        else:
            return res_json


# ASN lookup by IP address
def get_asn_from_endpoint(endpoint):
    asn = holder = None
    base_uri = 'https://stat.ripe.net'; url = '%s/data/prefix-overview/data.json'%base_uri
    params = {'resource' : endpoint}
    try: res = get_json_resource_from_absolute_uri(url, params)
    except Exception as e: print >> sys.stderr, e; return None
    try:
        asns_holders = []
        for item in res['data']['asns']:
            asn = item['asn']; holder = item['holder']
            asns_holders.append((asn, holder))
    except Exception as e: print >> sys.stderr, e
    return asns_holders


# AS holder lookup by ASN
def get_holder_from_asn(asn):
    base_uri = 'https://stat.ripe.net'; url = '%s/data/as-overview/data.json'%base_uri
    params = {'resource' : asn}
    try: res = get_json_resource_from_absolute_uri(url, params)
    except Exception as e: print >> sys.stderr, e; return None
    try:
        holder = res['data']['holder']
    except Exception as e: print >> sys.stderr, e
    return holder


# Reverse DNS lookup
def get_hostname_from_endpoint(endpoint):
    base_uri = 'https://stat.ripe.net'; url = '%s/data/reverse-dns-ip/data.json'%base_uri
    params = {'resource' : endpoint}
    try: res = get_json_resource_from_absolute_uri(url, params)
    except Exception as e: print >> sys.stderr, e; return None
    try:
        hostnames = []
        if res['data']['result'] is not None:  # result might be None here, i.e. no hostname could be found
            for item in res['data']['result']:
                hostnames.append(item)
    except Exception as e: print >> sys.stderr, e
    return hostnames


""" --- B A T C H --- """

# ==============================================
# lookup of destination AS numbers and hostnames
# ==============================================

with codecs.open('netflix_endpoint_to_asn.csv', 'w', 'utf-8') as f:
    f.write('%s;%s;%s\n' % ('ip', 'asn', 'holder'))  # header line

    conn = sqlite3.connect(DB_PATH)
    
    destinations = pd.read_sql_query('select distinct address from netflix', conn)
    endpoints = pd.read_sql_query('select distinct endpoint from traceroute', conn)  # !!! NOTE: this will result in more IP addresses than required; restricting this to the destination of the traceroute measurement only is likely sufficient
    conn.close()
     
    addresses = destinations['address'].append(endpoints['endpoint']).unique()

    for address in addresses:
        asns_holders = get_asn_from_endpoint(address)  # perform lookup
        for asn, holder in asns_holders:  # loop in case an IP has multiple associations
            f.write('%s;%d;%s\n'%(address, asn, holder))  # write 3-tuple to log file