# 调用
from protobuf_inspector.types import StandardParser
import io

parser = StandardParser()
fh = bytes.fromhex('088d111001180022230a2108bf9eb3fd0210001a173805c20112e593aae9878ce79c8be588b0e79a84efbc9f')
file_obj = io.BytesIO(fh)
output = parser.parse_message(file_obj, "message")
print(output)
