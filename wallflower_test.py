# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 11:53:27 2015

@author: eric
"""

__version__ = '0.0.1'

from wallflower_packet import WallflowerPacket, WallflowerMultiplePackets
from wallflower_schema import WallflowerSchema
import copy
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
            'value': "Hello",
            'at': '2016-02-21T18:13:13.0Z'
        },
        {
            'value': "World",
            'at': '2016-02-21T18:13:13.0Z'
        },
    ]
}
points_details = {
    'points-type': 's',
    'points-length': 0
}
validated_request, message_packet = ws.validatePointsRequest(points_request,'update',points_details)
print "Check Points Update Request:",
if validated_request:
    print "OK"
else:
    print "Error"
    print message_packet

# Points Update Request
points_request = {
    'points': [
        {
            'value': 0,
            'at': '2016-02-21T18:13:13.0Z'
        },
        {
            'value': 1,
            'at': '2016-02-21T18:13:13.0Z'
        },
    ]
}
points_details = {
    'points-type': 'i',
    'points-length': 0,
    'points-options': [
        {'option-value':0},
        {'option-value':1}
    ]
}
validated_request, message_packet = ws.validatePointsRequest(points_request,'update',points_details)
print "Check Points Update Request with Options:",
if validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
# Points Update Request
points_request = {
    'points': [
        {
            'value': 2,
            'at': '2016-02-21T18:13:13.0Z'
        },
        {
            'value': 1,
            'at': '2016-02-21T18:13:13.0Z'
        },
    ]
}
points_details = {
    'points-type': 'i',
    'points-length': 0,
    'points-options': [
        {'option-value':0},
        {'option-value':1}
    ]
}
validated_request, message_packet = ws.validatePointsRequest(points_request,'update',points_details)
print "Check Points Update Request with Value not in Options:",
if not validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
    
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
    'points-type': 's',
    'points-length': 0
}
validated_request, message_packet = ws.validatePointsRequest(points_request,'update',points_details)
print "Check Points Update Request with Invalid Types:",
if not validated_request:
    print "OK"
else:
    print "Error"
    print message_packet

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
    'points-type': 'i',
    'points-length': 0,
    'points-max': 10
}
validated_request, message_packet = ws.validatePointsRequest(points_request,'update',points_details)
print "Check Points Update Request that Violates Max:",
if not validated_request:
    print "OK"
else:
    print "Error"
    print message_packet

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
    'points-type': 'i',
    'points-length': 0,
    'points-min': 13
}
validated_request, message_packet = ws.validatePointsRequest(points_request,'update',points_details)
print "Check Points Update Request that Violates Min:",
if not validated_request:
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
print "Check Points Update Request with Invalid Timestamp:",
if not validated_request:
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

# Points Search Request
points_request = {
    'points': {
        'limit': -1, # Will not raise error, just be filtered
        'start': '2016-02-21T18:13:13.0Z',
        'end': '2016-02-21T18:13:13.0Z'
    }
}
points_details = {
    'points-type': 's'
}
validated_request, message_packet = ws.validatePointsRequest(points_request,'search',points_details)
print "Check Points Search Request with Invalid Limit:",
if validated_request:
    print "OK"
else:
    print "Error"
    print message_packet

# Points Search Request
points_request = {
    'points': {
        'start': '2016-02-20T18:13:13',
        'end': '2016-02-21T18:13:13.0Z'
    }
}
points_details = {
    'points-type': 's'
}
validated_request, message_packet = ws.validatePointsRequest(points_request,'search',points_details)
print "Check Points Search Request with Invalid Start:",
if not validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
# Points Search Request
points_request = {
    'points': {
        'start': '2016-02-22T18:13:13.0Z',
        'end': '2016-02-21T18:13:13.0Z'
    }
}
points_details = {
    'points-type': 's'
}
validated_request, message_packet = ws.validatePointsRequest(points_request,'search',points_details)
print "Check Points Search Request with Invalid Start/End:",
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

# Stream Create Request
stream_request = {
    'stream-id': 'test',
    'stream-details':{
        'stream-name': 'Test Stream',
        'stream-type': 'data'
    },
    'points-details':{
        'points-length': 0,
        'points-type': 'i',
        'points-options':[
            {
                'option-value': 1,
                'option-name': 'One'               
            },
            {
                'option-value': 2,
                'option-name': 'Two'               
            },
            {
                'option-value': 3,
                'option-name': 'Three'               
            }  
        ]
    }
}
validated_request, message_packet = ws.validateStreamRequest(stream_request,'create')
print "Check Stream Create Request with Options:",
if validated_request:
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
        'points-type': 'i',
        'points-options':[
            {
                'option-value': 1,
                'option-name': 'One'               
            },
            {
                'option-value': 2,
                'option-name': 'Two'               
            },
            {
                'option-value': '3',
                'option-name': 'Three'               
            }  
        ]
    }
}
validated_request, message_packet = ws.validateStreamRequest(stream_request,'create')
print "Check Stream Create Request with Invalid Options:",
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
        'points-type': 'i',
        'points-min': 0,
        'points-max': 2
    }
}
validated_request, message_packet = ws.validateStreamRequest(stream_request,'create')
print "Check Stream Create Request with Min/Max:",
if validated_request:
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
        'points-type': 'i',
        'points-min': 0,
        'points-max': '1'
    }
}
validated_request, message_packet = ws.validateStreamRequest(stream_request,'create')
print "Check Stream Create Request with Invalid Min/Max:",
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
        'points-type': 's',
        'points-min': 0,
    }
}
validated_request, message_packet = ws.validateStreamRequest(stream_request,'create')
print "Check Stream Create Request with Min for non-Int/Float:",
if not validated_request:
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
print "Check Stream Create Request with Invalid Stream ID:",
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
print "Check Stream Create Request with Invalid Points Type:",
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
print "Check Object Create Request with Invalid Object ID:",
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
print "Check Network Create Request with Invalid Network ID:",
if not validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
    
    

    
# Account Update Request
account_request = {
    'account-id': 'test',
    'account-details':{
        'account-name': 'Test Account',
    },
}
validated_request, message_packet = ws.validateAccountRequest(account_request,'update')
print "Check Account Update Request:",
if validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
account_request = {
    'account-id': 'test@#"',
    'account-details':{
        'account-name': 'Test Account'
    }
}
validated_request, message_packet = ws.validateAccountRequest(account_request,'create')
print "Check Account Update Request with Invalid Account ID:",
if not validated_request:
    print "OK"
else:
    print "Error"
    print message_packet
    
    
print
print "Single Response Schema"
print

account_response = {
    "account-code": 200,
    "account-message": "Success Message",
    "account-id": "test-account", 
    "account-details": {
        "account-keys": [
            {
                "type": "read",
                "key": "13c8b0ff4ffb423295a6c2990c18fd6d"
            }
        ], 
        "account-name": "Test Account", 
        "account-master-key": "b6d62510688b4168a74503459fb83d7f", 
        "account-owner": "Owner"
    }, 
    "networks": {
        "test-network": {
            "network-id": "test-network",
            "network-details": {
                "network-name": "Test Network",
                "network-keys": [
                    {
                        "type": "read",
                        "key": "4c5d451da7d8483889522e5ebe7c449a"
                    }
                ], 
                "network-owner": "Owner", 
                "network-master-key": "771f5b3b39624e8992a731ff793f883d"
            },
            "objects": {
                "test-object": {
                    "object-id": "test-network",
                    "object-details": {
                        "object-name": "Test Object",
                        "object-keys": [
                            {
                                "type": "read",
                                "key": "4c5d451da7d8483889522e5ebe7c449a"
                            }
                        ], 
                        "object-owner": "Owner", 
                        "object-master-key": "771f5b3b39624e8992a731ff793f883d"
                    },
                    "streams": {
                        "test-stream": {
                            "stream-id": "test-stream",
                            "stream-details": {
                                "stream-name": "Test Stream",
                                "stream-keys": [
                                    {
                                        "type": "read",
                                        "key": "4c5d451da7d8483889522e5ebe7c449a"
                                    }
                                ], 
                                "stream-owner": "Owner", 
                                "stream-master-key": "771f5b3b39624e8992a731ff793f883d"
                            },
                            "points-details": {
                                'points-type': 'i',
                                'points-length': 0,
                                'points-min': 13
                            },
                            "points": []
                        }
                    }
                }
            }
        }
    }
}

validated_request, message_packet = ws.validateAccountResponse(account_response,'read')
print "Check Account Read Response with Keys Removed:",
if validated_request:
    print "OK"
    #print validated_request
else:
    print "Error"
    print message_packet
    
network_response = copy.deepcopy( account_response['networks']['test-network'] )
network_response['network-code'] = 200
network_response['network-message'] = "Success Message"
validated_request, message_packet = ws.validateNetworkResponse(network_response,'read')
print "Check Network Read Response with Keys Removed:",
if validated_request:
    print "OK"
    #print validated_request
else:
    print "Error"
    print message_packet

object_response = copy.deepcopy( network_response['objects']['test-object'] )
object_response['object-code'] = 200
object_response['object-message'] = "Success Message"
validated_request, message_packet = ws.validateObjectResponse(object_response,'read')
print "Check Object Read Response with Keys Removed:",
if validated_request:
    print "OK"
    #print validated_request
else:
    print "Error"
    print message_packet

stream_response = copy.deepcopy( object_response['streams']['test-stream'] )
stream_response['stream-code'] = 200
stream_response['stream-message'] = "Success Message"
validated_request, message_packet = ws.validateStreamResponse(stream_response,'read')
print "Check Stream Read Response with Keys Removed:",
if validated_request:
    print "OK"
    #print validated_request
else:
    print "Error"
    print message_packet
    
points_response = copy.deepcopy( stream_response )
del( points_response['stream-details'] )
del( points_response['stream-code'] )
del( points_response['stream-message'] )
points_response['points-code'] = 200
points_response['points-message'] = "Success Message"
validated_request, message_packet = ws.validatePointsResponse(points_response,'read')
print "Check Points Read Response with Keys Removed:",
if validated_request:
    print "OK"
    #print validated_request
else:
    print "Error"
    print message_packet
    
    

print
print "Single Packet Request"
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
    print wp.schema_request


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
    print wp.schema_request


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
    print wp.schema_request


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
    print wp.schema_request
    
    
# Account Update Packet
account_request = {
    'account-id': 'test',
    'account-details':{
        'account-name': 'Test Account',
    },
}
valid = wp.loadAccountRequest(account_request, 'update')
has = wp.hasAccountRequest()
print "Check Account Update Packet:", 
if valid and has:
    print "OK"
else:
    print "Error"
    print wp.schema_request
    
    
    
    
    
    
print
print "Single Packet Response"
print
    
# Points Read Packet
valid = wp.checkPointsResponse(points_response, 'read')
print "Check Points Read Response Packet:",
if valid:
    print "OK"
else:
    print "Error"
    print wp.schema_response

# Stream Read Packet
valid = wp.checkStreamResponse(stream_response, 'read')
print "Check Stream Read Response Packet:",
if valid:
    print "OK"
else:
    print "Error"
    print wp.schema_response


# Object Read Packet
valid = wp.checkObjectResponse(object_response, 'read')
print "Check Object Read Response Packet:",
if valid:
    print "OK"
else:
    print "Error"
    print wp.schema_response

# Network Read Packet
valid = wp.checkNetworkResponse(network_response, 'read')
print "Check Network Read Response Packet:",
if valid:
    print "OK"
else:
    print "Error"
    print wp.schema_response

# Account Read Packet
valid = wp.checkAccountResponse(account_response, 'read')
print "Check Account Read Response Packet:",
if valid:
    print "OK"
else:
    print "Error"
    print wp.schema_response
    
    
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