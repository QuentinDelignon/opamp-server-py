import io
import importlib
from google.protobuf.json_format import MessageToDict , MessageToJson
from fastapi.logger import logger
from google.protobuf import symbol_database
import json

# Get the global symbol database
sym_db = symbol_database.Default()

def load_pb2_modules(module_names):
    """
    Load protobuf modules and register their types with the symbol database.
    
    Args:
        module_names: List of module names (e.g., "agent_pb2")
    """
    for module_name in module_names:
        try:
            importlib.import_module(module_name)
            logger.info(f"Loaded protobuf module: {module_name}")
        except ImportError as e:
            logger.error(f"Failed to import module {module_name}: {e}")

def decode_varint(buffer):
    """
    Decode a Base 128 Varint from a buffer.
    
    Args:
        buffer: BytesIO buffer containing the varint
        
    Returns:
        Tuple of (value, bytes_read)
    """
    result = 0
    shift = 0
    bytes_read = 0
    
    while True:
        byte = buffer.read(1)
        if not byte:
            raise ValueError("Unexpected end of buffer while decoding varint")
        
        bytes_read += 1
        i = ord(byte)
        result |= (i & 0x7f) << shift
        shift += 7
        
        if not (i & 0x80):
            break
            
    return result, bytes_read

def decode_opamp_message(data):
    """
    Decode an OpAMP WebSocket message according to the OpAMP specification.
    
    Args:
        data: Raw binary data from WebSocket
        
    Returns:
        Tuple of (header_value, protobuf_message_dict, message_type) or (header_value, None, None)
    """
    buffer = io.BytesIO(data)
    
    # Decode the header (Base 128 Varint)
    header_value, header_bytes_read = decode_varint(buffer)
    
    # Check header value is 0 per specification
    if header_value != 0:
        logger.warning(f"Invalid OpAMP header value: {header_value}, expected 0")
        return header_value, None, None
    
    # Calculate payload size
    total_size = len(data)
    payload_size = total_size - header_bytes_read
    
    # Read payload bytes - the buffer's current position is already after the header
    # because we read the header from the buffer above
    payload = buffer.read(payload_size)
    
    # Handle empty payload case
    if not payload:
        logger.info("Empty payload detected (valid per OpAMP spec)")
        return header_value, {}, None
    
    # Try to decode the payload with each registered protobuf message type
    for descriptor , _ in sym_db._classes.items(): # type: ignore
        if not descriptor.full_name.startswith('opamp'):
            continue
        try:
            # Create an instance of this message type
            message = sym_db.GetPrototype(descriptor)()
            
            # Try to parse the binary data
            message.ParseFromString(payload)
            
            # If we get here, parsing was successful
            message_dict = MessageToDict(
                message,
                descriptor_pool=sym_db.pool,
                preserving_proto_field_name=True
            )
            
            return header_value, message_dict, descriptor.full_name
        except Exception as e:
            #traceback.print_exc()
            #print(f"decode Error: {type(e)} -> {repr(e)}")
            continue
    
    logger.warning("Could not identify protobuf message type for payload")
    return header_value, None, None