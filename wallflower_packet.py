#####################################################################################
#
#  Copyright (C) Eric Burger, Wallflower.cc
#
#  Should you enter into a separate license agreement after having received a copy of
#  this software, then the terms of such license agreement replace the terms below at
#  the time at which such license agreement becomes effective.
#
#  In case a separate license agreement ends, and such agreement ends without being
#  replaced by another separate license agreement, the license terms below apply
#  from the time at which said agreement ends.
#
#  LICENSE TERMS
#
#  This program is free software: you can redistribute it and/or modify it under the
#  terms of the GNU Affero General Public License, version 3, as published by the
#  Free Software Foundation. This program is distributed in the hope that it will be
#  useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#  See the GNU Affero General Public License Version 3 for more details.
#
#  You should have received a copy of the GNU Affero General Public license along
#  with this program. If not, see <http://www.gnu.org/licenses/agpl-3.0.en.html>.
#
#####################################################################################

__version__ = '0.0.2'

from wallflower_schema import WallflowerSchema
import json
import copy

class WallflowerPacketBase:
    
    raw_request = None
    request = None
    response = None
    validated_request = None
    validated_response = None
    schema_request = None
    schema_response = None
    request_list = []
    request_type = None
    request_level = None
        
        
class WallflowerPacket(WallflowerPacketBase):

    '''
    Load single request packet. Return False if there is an error.
    '''
    def loadRequest(self,packet,request_type,request_level):
        try:
            # Store paclet
            self.request = packet
            self.request_type = request_type
            self.request_level = request_level
            
            if request_level == 'account':
                # Validate packet contents
                self.validated_request, self.schema_request = \
                    WallflowerSchema().validateAccountRequest(self.request,request_type)
                return self.schema_request['account-valid-request']
            elif request_level == 'network':
                # Validate packet contents
                self.validated_request, self.schema_request = \
                    WallflowerSchema().validateNetworkRequest(self.request,request_type)
                return self.schema_request['network-valid-request']
            elif request_level == 'object':
                # Validate packet contents
                self.validated_request, self.schema_request = \
                    WallflowerSchema().validateObjectRequest(self.request,request_type)
                return self.schema_request['object-valid-request']
            elif request_level == 'stream':
                # Validate packet contents
                self.validated_request, self.schema_request = \
                    WallflowerSchema().validateStreamRequest(self.request,request_type)
                return self.schema_request['stream-valid-request']
            elif request_level == 'points':
                # Validate packet contents
                self.validated_request, self.schema_request = \
                    WallflowerSchema().validatePointsRequest(self.request,request_type)
                return self.schema_request['points-valid-request']
            else:
                return False
        except:
            return False
    
    '''
    Check single response packet. Return False if there is an error.
    '''
    def checkResponse(self,packet,request_type,request_level):
        try:
            # Store paclet
            self.response = packet
            self.request_type = request_type
            self.request_level = request_level
            
            if request_level == 'account':
                # Validate packet contents
                self.validated_response, self.schema_response = \
                    WallflowerSchema().validateAccountResponse(self.response,request_type)
                return self.schema_response['account-valid-response']
            elif request_level == 'network':
                # Validate packet contents
                self.validated_response, self.schema_response = \
                    WallflowerSchema().validateNetworkResponse(self.response,request_type)
                return self.schema_response['network-valid-response']
            elif request_level == 'object':
                # Validate packet contents
                self.validated_response, self.schema_response = \
                    WallflowerSchema().validateObjectResponse(self.response,request_type)
                return self.schema_response['object-valid-response']
            elif request_level == 'stream':
                # Validate packet contents
                self.validated_response, self.schema_response = \
                    WallflowerSchema().validateStreamResponse(self.response,request_type)
                return self.schema_response['stream-valid-response']
            elif request_level == 'points':
                # Validate packet contents
                self.validated_response, self.schema_response = \
                    WallflowerSchema().validatePointsResponse(self.response,request_type)
                return self.schema_response['points-valid-response']
            else:
                return False
        except:
            return False
            
            
    '''
    Load account packet. Return False if error or packet does not contain request.
    '''
    def loadAccountRequest(self,packet,request_type):
        return self.loadRequest(packet,request_type,'account')
        
    '''
    Load network packet. Return False if error or packet does not contain request.
    '''
    def loadNetworkRequest(self,packet,request_type):
        return self.loadRequest(packet,request_type,'network')

    '''
    Load object packet. Return False if error or packet does not contain request.
    '''
    def loadObjectRequest(self,packet,request_type):
        return self.loadRequest(packet,request_type,'object')
        
    '''
    Load stream packet. Return False if error or packet does not contain request.
    '''
    def loadStreamRequest(self,packet,request_type):
        return self.loadRequest(packet,request_type,'stream')
        
    '''
    Load points packet. Return False if error or packet does not contain request.
    '''
    def loadPointsRequest(self,packet,request_type):
        return self.loadRequest(packet,request_type,'points')
        
    '''
    Check if the packet contains a valid request. 
    '''
    def hasRequest(self,request_level):
        if request_level+'-valid-request' in self.schema_request and \
            self.schema_request[request_level+'-valid-request']:
            return True, self.validated_request
        else:
            return False, self.schema_request

    '''
    Check if the packet contains a valid account request. 
    '''
    def hasAccountRequest(self):
        return self.hasRequest('account')
        
    '''
    Check if the packet contains a valid network request. 
    '''
    def hasNetworkRequest(self):
        return self.hasRequest('network')
            
    '''
    Check if the packet contains a valid object request. 
    '''
    def hasObjectRequest(self):
        return self.hasRequest('object')

    '''
    Check if the packet contains a valid stream request. 
    '''
    def hasStreamRequest(self):
        return self.hasRequest('stream')
            
    '''
    Check if the packet contains a valid points request. 
    '''
    def hasPointsRequest(self):
        return self.hasRequest('points')
        
        
    '''
    Check account response. Return False if error or packet does not contain response.
    '''
    def checkAccountResponse(self,packet,request_type):
        return self.checkResponse(packet,request_type,'account')
        
    '''
    Check network response. Return False if error or packet does not contain response.
    '''
    def checkNetworkResponse(self,packet,request_type):
        return self.checkResponse(packet,request_type,'network')

    '''
    Check object response. Return False if error or packet does not contain response.
    '''
    def checkObjectResponse(self,packet,request_type):
        return self.checkResponse(packet,request_type,'object')
        
    '''
    Check stream response. Return False if error or packet does not contain response.
    '''
    def checkStreamResponse(self,packet,request_type):
        return self.checkResponse(packet,request_type,'stream')
        
    '''
    Check points response. Return False if error or packet does not contain response.
    '''
    def checkPointsResponse(self,packet,request_type):
        return self.checkResponse(packet,request_type,'points')
        
        
        
        
        
        
        
class WallflowerMultiplePackets(WallflowerPacketBase):
    
    '''
    Load packet(s). Return False if error or packet does not contain request.
    Allow partially-valid request (invalid requests will be removed, if possible) 
    '''
    def loadRequests(self,packet,request_type):
        try:
            # Store paclet
            self.packet = packet
            self.request_type = request_type
            self.request_level = None
            
            # Validate packet contents
            self.validated_request, self.schema_request = WallflowerSchema().validateMultipleRequests(self.packet,request_type,True)
            
            return True
        except:
            return False
            
    '''
    Load packet. Return False if error or packet does not contain request.
    Allow partially-valid request (invalid requests will be removed, if possible) 
    '''
    """
    def loadJSONRequest(self,json_packet,request_type):
        try:
            # Store paclet
            packet = json.loads(json_packet)
            # Validate packet contents
            return self.loadRequest(packet,request_type)
        except:
            return False
    """
    
    '''
    Check if packet contains valid request. Only for multiple request packets.
    '''
    def hasAnyRequest(self):
        if 'valid-request' in self.schema_request and self.schema_request['valid-request']:
            return True
        else:
            return False
            
    '''
    Route has[__]Request requests    
    '''
    def hasRequest(self,request_level,ids):
        if request_level == 'network':
            network_id = ids[0]
            return self.hasNetworkRequest(network_id)
        elif request_level == 'object':
            network_id,object_id = ids
            return self.hasObjectRequest(network_id,object_id)
        elif request_level == 'stream':
            network_id,object_id,stream_id = ids
            return self.hasStreamRequest(network_id,object_id,stream_id)
        elif request_level == 'points':
            network_id,object_id,stream_id = ids
            return self.hasPointsRequest(network_id,object_id,stream_id)
            
    '''
    Returns network id
    '''
    def getNetworkID(self):
        try:
            return self.validated_request['network-id']
        except:
            return None
            
    '''
    Check for objects
    '''
    def hasObjectIDs(self):
        try:
            return (len(self.validated_request['objects'])>0)
        except:
            return False
            
    '''
    Returns list of object ids
    '''
    def getObjectIDs(self):
        try:
            return self.validated_request['objects'].keys()
        except:
            return []
            
    '''
    Check for streams
    '''
    def hasStreamIDs(self,object_id):
        try:
            return (len(self.validated_request['objects'][object_id]['streams'])>0)
        except:
            return False
            
    '''
    Returns list of object ids
    '''
    def getStreamIDs(self,object_id):
        try:
            return self.validated_request['objects'][object_id]['streams'].keys()
        except:
            return []
                        
    '''
    Check if packet contains valid request.
    Returns a deep copy of the request (to allow changes not to alter the original request).
    '''
    def hasNetworkRequest(self,network_id):
        try:
            include = ()
            if self.request_type in ['create','update']:
                assert 'network-details' in self.validated_request
                include = ('network-id', 'network-details')
                return True, copy.deepcopy({k: self.validated_request[k] for k in ('network-id', 'network-details')})
            elif self.request_type in ['read','delete','search']:
                assert all(k not in self.validated_request for k in ['network-details','objects'])
                include = ('network-id', )
                           
            #network_request = copy.deepcopy( 
            #    {k: self.validated_request[k] for k in include}
            #)
            # Create copy
            network_request = json.loads(json.dumps( 
                {k: self.validated_request[k] for k in include}
            ))
            
            return True, network_request
        except:
            pass
        return False, {}
            
    '''
    Check if packet contains valid request
    Returns a deep copy of the request (to allow changes not to alter the original request).
    '''
    def hasObjectRequest(self, network_id, object_id):
        try:
            include = ()
            if self.request_type in ['create','update']:
                assert 'object-details' in self.validated_request['objects'][object_id]
                include = ('object-id', 'object-details')
            elif self.request_type in ['read','delete','search']:
                assert all(k not in self.validated_request['objects'][object_id] for k in ['object-details','streams'])
                include = ('object-id', )

            #object_request = copy.deepcopy( 
            #    {k: self.validated_request['objects'][object_id][k] for k in include}
            #)
            # Create copy
            object_request = json.loads(json.dumps( 
                {k: self.validated_request['objects'][object_id][k] for k in include}
            ))
            request= {
                    "network-id": network_id,
                    "objects": {
                        object_id: object_request
                    }
            } 
            return True, request
        except:
            pass
        return False, {}
            
    '''
    Check if packet contains valid request
    '''
    def hasStreamRequest(self, network_id, object_id, stream_id):
        try:
            include = ()
            if self.request_type in ['create']:
                assert 'stream-details' in self.validated_request['objects'][object_id]['streams'][stream_id]
                include = ('stream-id', 'stream-details', 'points-details')
            elif self.request_type in ['update']:
                assert 'stream-details' in self.validated_request['objects'][object_id]['streams'][stream_id]
                include = ('stream-id', 'stream-details')
            elif self.request_type in ['read','delete','search']:
                assert all(k not in self.validated_request['objects'][object_id]['streams'][stream_id] for k in ['stream-details','points'])
                include = ('stream-id', )
                
            #stream_request = copy.deepcopy( 
            #    {k: self.validated_request['objects'][object_id]['streams'][stream_id][k] for k in include}
            #)
            # Create copy
            stream_request = json.loads(json.dumps( 
                {k: self.validated_request['objects'][object_id]['streams'][stream_id][k] for k in include}
            ))
            request = {
                "network-id": network_id,
                "objects": {
                    object_id: {
                        "object-id": object_id,
                        "streams": {
                            stream_id: stream_request
                        }                                
                    } 
                }
            }
            return True, request
        except:
            pass
        return False, {}

    '''
    Check if packet contains valid request
    Returns a copy of the request (to allow changes not to alter the original request).
    '''
    def hasPointsRequest(self, network_id, object_id, stream_id):
        try:
            assert self.request_type in ['update','read','search']
            #points_request = copy.deepcopy( 
            #    self.validated_request['objects'][object_id]['streams'][stream_id]['points']
            #)
            # Create copy
            points_request = json.loads(json.dumps( 
                self.validated_request['objects'][object_id]['streams'][stream_id]['points']
            ))
            request = {
                "network-id": network_id,
                "objects": {
                    object_id: {
                        "object-id": object_id,
                        "streams": {
                            stream_id: { 
                                "stream-id": stream_id,
                                "points": points_request
                            }
                        }                                
                    } 
                }
            }
            return True, request
        except:
            pass
        return False, {}

