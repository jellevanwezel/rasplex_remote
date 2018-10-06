#!/usr/bin/python
import sys
import re
import os
import urllib2

host = "127.0.0.1"
port = "3005"
key_map = {
    "exit":"Input.Back",
    "F4 (yellow)":"NextSubtitle",
    "F1 (blue)":"AudioNextLanguage",
    "forward":"Player.Seek",
    "backward":"Player.Seek",
    "Fast forward":"Player.Seek",
    "rewind":"Player.Seek",
    "contents menu":"Input.ContextMenu",
    "play":"Player.PlayPause",
    "pause":"Player.PlayPause",
}

params_map = {
    "Fast forward":'"value":"smallforward", "playerid":1',
    "rewind":'"value":"smallbackward", "playerid":1',
    "play":'"playerid":1',
    "pause":'"playerid":1',
    "forward":'"value":100, "playerid":1',
    "backward":'"value":0, "playerid":1',
}

def send_action(key):
    action = key_map[key] if key in key_map else "Input." + key
    params = ',"params":{{ {0} }}'.format(params_map[key]) if key in params_map else ""
    url_str = 'http://{0}:{1}/jsonrpc?request={{"jsonrpc":"2.0","id":1,"method":"{2}" {3} }}'.format(host,port,action,params)
    result = urllib2.urlopen(url_str).read()
    print(result)

print "starting"
while 1:
    line = sys.stdin.readline()
    #sys.stdout.write(line)
    searchObj = re.search( r'^.*key pressed\:\s(.*)\s\(.*,\s0\)$', line, re.M|re.I)
    if searchObj:
        key = searchObj.group(1)
        sys.stdout.write("Sending " + searchObj.group(1))
        sys.stdout.write("\n")
        send_action(key)
