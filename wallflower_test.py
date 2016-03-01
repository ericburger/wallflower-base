# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 11:53:27 2015

@author: eric
"""

__version__ = '0.0.1'

from wallflower_packet import *
from wallflower_schema import *
#import datetime

ws = WallflowerSchema()

wp = WallflowerPacket()

wmp = WallflowerMultiplePackets()

print
print "Single Request Schema"
print

# Points Update Request
points_request = {
    'points': [
        {
            'value': 12,
            'at': '2016-02-21T18:13:13.0Z'
        },
        {
            'value': 14,
            'at': '2016-02-21T18:13:13.0Z'
        },
    ]
}
points_details = {
    'points-type': 's'
}
validated_request, message_packet = ws.validatePointsRequest(points_request,'update',points_details)
print "Check Points Update Request:",
if validated_request:
    print "OK"
else:
    print "Error"
    print message_packet

# Points Search Request
points_request = {
    'points': {
        'limit': 10,
        'start': '2016-02-21T18:13:13.0Z',
        'end': '2016-02-21T18:13:13.0Z'
    }
}
points_details = {
    'points-type': 's'
}
validated_request, message_packet = ws.validatePointsRequest(points_request,'search',points_details)
print "Check Points Search Request:",
if validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
points_request = {
    'points': [
        {
            'value': 12,
            'at': '2016-02-21T18:13:13.0Z'
        },
        {
            'value': 14,
            'at': '2016-02-21T18:13:13.0'
        },
    ]
}
points_details = {
    'points-type': 's'
}
validated_request, message_packet = ws.validatePointsRequest(points_request,'update',points_details)
print "Check Invalid Timestamp:",
if not validated_request:
    print "OK"
else:
    print "Error"
    print message_packet




# Stream Create Request
stream_request = {
    'stream-id': 'test',
    'stream-details':{
        'stream-name': 'Test Stream',
        'stream-type': 'data'
    },
    'points-details':{
        'points-length': 0,
        'points-type': 'i'
    }
}
validated_request, message_packet = ws.validateStreamRequest(stream_request,'create')
print "Check Stream Create Request:",
if validated_request:
    print "OK"
else:
    print "Error"
    print message_packet

# Stream Update Request
stream_request = {
    'stream-id': 'test',
    'stream-details':{
        'stream-name': 'Test Stream',
        'stream-type': 'data'
    },
}
validated_request, message_packet = ws.validateStreamRequest(stream_request,'update')
print "Check Stream Update Request:",
if validated_request:
    print "OK"
else:
    print "Error"
    print message_packet

stream_request = {
    'stream-id': 'test@#',
    'stream-details':{
        'stream-name': 'Test Stream',
        'stream-type': 'data'
    },
    'points-details':{
        'points-length': 0,
        'points-type': 'i'
    }
}
validated_request, message_packet = ws.validateStreamRequest(stream_request,'create')
print "Check Invalid Stream ID:",
if not validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
stream_request = {
    'stream-id': 'test',
    'stream-details':{
        'stream-name': 'Test Stream',
        'stream-type': 'data'
    },
    'points-details':{
        'points-length': 0,
        'points-type': 'g'
    }
}
validated_request, message_packet = ws.validateStreamRequest(stream_request,'create')
print "Check Invalid Points Type:",
if not validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
    
    

# Object Create Request
object_request = {
    'object-id': 'test',
    'object-details':{
        'object-name': 'Test Object'
    },
}
validated_request, message_packet = ws.validateObjectRequest(object_request,'create')
print "Check Object Create Request:",
if validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
# Object Update Request
object_request = {
    'object-id': 'test',
    'object-details':{
        'object-name': 'Test Object',
    },
}
validated_request, message_packet = ws.validateObjectRequest(object_request,'update')
print "Check Object Update Request:",
if validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
object_request = {
    'object-id': 'test@#"',
    'object-details':{
        'object-name': 'Test Object'
    }
}
validated_request, message_packet = ws.validateObjectRequest(object_request,'create')
print "Check Invalid Object ID:",
if not validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
    
    

# Network Create Request
network_request = {
    'network-id': 'test',
    'network-details':{
        'network-name': 'Test Network'
    },
}
validated_request, message_packet = ws.validateNetworkRequest(network_request,'create')
print "Check Network Create Request:",
if validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
# Network Update Request
network_request = {
    'network-id': 'test',
    'network-details':{
        'network-name': 'Test Network',
    },
}
validated_request, message_packet = ws.validateNetworkRequest(network_request,'update')
print "Check Network Update Request:",
if validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
network_request = {
    'network-id': 'test@#"',
    'network-details':{
        'network-name': 'Test Network'
    }
}
validated_request, message_packet = ws.validateNetworkRequest(network_request,'create')
print "Check Invalid Network ID:",
if not validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
    
    
print
print "Single Packet"
print
    
# Points Update Packet
points_request = {
    'points': [
        {
            'value': 12,
            'at': '2016-02-21T18:13:13.0Z'
        },
        {
            'value': 14,
            'at': '2016-02-21T18:13:13.0Z'
        },
    ]
}
valid = wp.loadPointsRequest(points_request, 'update')
has = wp.hasPointsRequest()
print "Check Points Update Packet:",
if valid and has:
    print "OK"
else:
    print "Error"
    print wp.schema_packet


# Stream Create Packet
stream_request = {
    'stream-id': 'test',
    'stream-details':{
        'stream-name': 'Test Stream',
        'stream-type': 'data'
    },
    'points-details':{
        'points-length': 0,
        'points-type': 'i'
    }
}
valid = wp.loadStreamRequest(stream_request, 'create')
has = wp.hasStreamRequest()
print "Check Stream Create Packet:", 
if valid and has:
    print "OK"
else:
    print "Error"
    print wp.schema_packet


# Object Update Packet
object_request = {
    'object-id': 'test',
    'object-details':{
        'object-name': 'Test Object',
    },
}
valid = wp.loadObjectRequest(object_request, 'update')
has = wp.hasObjectRequest()
print "Check Object Update Packet:", 
if valid and has:
    print "OK"
else:
    print "Error"
    print wp.schema_packet


# Network Update Packet
network_request = {
    'network-id': 'test',
    'network-details':{
        'network-name': 'Test Network',
    },
}
valid = wp.loadNetworkRequest(network_request, 'create')
has = wp.hasNetworkRequest()
print "Check Network Create Packet:", 
if valid and has:
    print "OK"
else:
    print "Error"
    print wp.schema_packet
    
    
    
    
    
'''
search_request = {
  "network-id": "ce186",
  'objects': {
    "fridge": {
      "object-id": "fridge", 
      'streams': {
        "temperature": {
          "stream-id": "temperature",
          'points': {
            "limit":20
          },
        }
      }
    },
    "k": {
      "object-id": "k", 
      "streams": {}
    }
  }
}
print WallflowerSchema().validateRequest(search_request,'search',True)

p = WallflowerPacket()
print p.loadRequest(search_request, 'search')
print p.hasAnyRequest()
print p.hasPointsRequest("ce186","fridge","temperature")
'''