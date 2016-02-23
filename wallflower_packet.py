# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 11:53:27 2015

@author: eric burger
"""

__version__ = '0.0.1'

from wallflower_schema import WallflowerSchema
import json
import copy

class WallflowerPacket:
    
    raw_packet = None
    packet = None
    validated_packet = None
    message_packet = None
    request_list = []
    request_type = None
    
    c_type_info = {
        'b' : {
            'c_type' : 'signed char',
            'python_type' : int,
            'standard_size' : 1
        },
        '?' : {
            'c_type' : '_Bool',
            'python_type' : bool,
            'standard_size' : 1
        },
        'c' : {
            'c_type' : 'char',
            'python_type' : basestring,
            'standard_size' : 1
        },
        's' : {
            'c_type' : 'char[]',
            'python_type' : basestring,
            'standard_size' : 1
        },
        'B' : {
            'c_type' : 'unsigned char',
            'python_type' : int,
            'standard_size' : 1
        },
        'h' : {
            'c_type' : 'short',
            'python_type' : int,
            'standard_size' : 2
        },
        'H' : {
            'c_type' : 'unsigned short',
            'python_type' : int,
            'standard_size' : 2
        },
        'i' : {
            'c_type' : 'int',
            'python_type' : int,
            'standard_size' : 4
        },
        'I' : {
            'c_type' : 'unsigned int',
            'python_type' : int,
            'standard_size' : 4
        },
        'f' : {
            'c_type' : float,
            'python_type' : float,
            'standard_size' : 4
        },
        'q' : {
            'c_type' : 'long long',
            'python_type' : int,
            'standard_size' : 8
        },
        'Q' : {
            'c_type' : 'unsigned long long',
            'python_type' : int,
            'standard_size' : 8
        },
        'd' : {
            'c_type' : 'double',
            'python_type' : float,
            'standard_size' : 8
        }
    }

    def getPythonType(self,data_type):
        if isinstance(data_type,basestring):
            return self.c_type_info[data_type]['python_type']
        elif isinstance(data_type,int):
            return self.c_type_info[WallflowerSchema().data_type_list[data_type]]['python_type']
        return int
        
    '''
    Load packet. Return False if error or packet does not contain request.
    Allow partially-valid request (invalid requests will be removed, if possible) 
    '''
    def loadRequest(self,packet,request_type):
        try:
            # Store paclet
            self.packet = packet
            # Validate packet contents
            self.validated_packet, self.message_packet = WallflowerSchema().validateRequest(self.packet,request_type,True)
            self.request_type = request_type
            
            return True
        except:
            return False
            
    '''
    Load packet. Return False if error or packet does not contain request.
    Allow partially-valid request (invalid requests will be removed, if possible) 
    '''
    def loadJSONRequest(self,json_packet,request_type):
        try:
            # Store paclet
            packet = json.loads(json_packet)
            # Validate packet contents
            return self.loadRequest(packet,request_type)
        except:
            return False

    '''
    Check if packet contains valid request
    '''
    def hasAnyRequest(self):
        if 'valid-request' in self.message_packet and self.message_packet['valid-request']:
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
            return self.validated_packet['network-id']
        except:
            return None
            
    '''
    Check for objects
    '''
    def hasObjectIDs(self):
        try:
            return (len(self.validated_packet['objects'])>0)
        except:
            return False
            
    '''
    Returns list of object ids
    '''
    def getObjectIDs(self):
        try:
            return self.validated_packet['objects'].keys()
        except:
            return []
            
    '''
    Check for streams
    '''
    def hasStreamIDs(self,object_id):
        try:
            return (len(self.validated_packet['objects'][object_id]['streams'])>0)
        except:
            return False
            
    '''
    Returns list of object ids
    '''
    def getStreamIDs(self,object_id):
        try:
            return self.validated_packet['objects'][object_id]['streams'].keys()
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
                assert 'network-details' in self.validated_packet
                include = ('network-id', 'network-details')
                return True, copy.deepcopy({k: self.validated_packet[k] for k in ('network-id', 'network-details')})
            elif self.request_type in ['read','delete','search']:
                assert all(k not in self.validated_packet for k in ['network-details','objects'])
                include = ('network-id', )
                           
            #network_request = copy.deepcopy( 
            #    {k: self.validated_packet[k] for k in include}
            #)
            # Create copy
            network_request = json.loads(json.dumps( 
                {k: self.validated_packet[k] for k in include}
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
                assert 'object-details' in self.validated_packet['objects'][object_id]
                include = ('object-id', 'object-details')
            elif self.request_type in ['read','delete','search']:
                assert all(k not in self.validated_packet['objects'][object_id] for k in ['object-details','streams'])
                include = ('object-id', )

            #object_request = copy.deepcopy( 
            #    {k: self.validated_packet['objects'][object_id][k] for k in include}
            #)
            # Create copy
            object_request = json.loads(json.dumps( 
                {k: self.validated_packet['objects'][object_id][k] for k in include}
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
                assert 'stream-details' in self.validated_packet['objects'][object_id]['streams'][stream_id]
                include = ('stream-id', 'stream-details', 'points-details')
            elif self.request_type in ['update']:
                assert 'stream-details' in self.validated_packet['objects'][object_id]['streams'][stream_id]
                include = ('stream-id', 'stream-details')
            elif self.request_type in ['read','delete','search']:
                assert all(k not in self.validated_packet['objects'][object_id]['streams'][stream_id] for k in ['stream-details','points'])
                include = ('stream-id', )
                
            #stream_request = copy.deepcopy( 
            #    {k: self.validated_packet['objects'][object_id]['streams'][stream_id][k] for k in include}
            #)
            # Create copy
            stream_request = json.loads(json.dumps( 
                {k: self.validated_packet['objects'][object_id]['streams'][stream_id][k] for k in include}
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
            #    self.validated_packet['objects'][object_id]['streams'][stream_id]['points']
            #)
            # Create copy
            points_request = json.loads(json.dumps( 
                self.validated_packet['objects'][object_id]['streams'][stream_id]['points']
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

