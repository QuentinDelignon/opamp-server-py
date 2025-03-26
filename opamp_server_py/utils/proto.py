import io
from fastapi.logger import logger

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

def split_message(data : bytes) -> tuple[int,bytes | None]:
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
        return header_value, None
    
    # Calculate payload size
    total_size = len(data)
    payload_size = total_size - header_bytes_read
    
    # Read payload bytes - the buffer's current position is already after the header
    # because we read the header from the buffer above
    payload = buffer.read(payload_size)
    
    return header_value , payload