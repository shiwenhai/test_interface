#!/usr/bin/env python
#  -*- coding:utf-8 -*-
__author__ = 'songqi'

import ConfigParser
import urllib
import urllib2
import json

def getConfig(configType, configName):
    config = ConfigParser.ConfigParser()
    config.read("config\\interface.ini")
    return config.get(configType, configName)

def getAddress(configType):
    return getConfig(configType, "address")

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

def http_post(configType):
    url = getAddress(configType)
    #print "url:"+url
    #values = {"userId": "13291691",
    #          "bpId": "3136218"}
    #print "="*30
    values = {"userId": "13291691",
              "bpId": "3136218"}
    jdata = json.dumps(values)
    #print is_json(jdata)
    req = urllib2.Request(url, jdata, {"Content-Type": "application/json"})
    response = urllib2.urlopen(req)
    return response.read()

def getResult():
    reqa = http_post("dev")
    print "result: "+reqa
