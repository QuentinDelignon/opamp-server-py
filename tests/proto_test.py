from google.protobuf.json_format import MessageToDict

def test_symdb():
    from opamp_server_py.types.anyvalue_pb2 import _sym_db
    for desc , m in _sym_db._classes.items():
            message = _sym_db.GetPrototype(desc)()
            message.ParseFromString(b"")
            message_dict = MessageToDict(
                message,
                descriptor_pool=_sym_db.pool,
                preserving_proto_field_name=True
            )
            print(message_dict)