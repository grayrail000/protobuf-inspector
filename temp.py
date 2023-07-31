# 调用
from protobuf_inspector.types import StandardParser
from protobuf_inspector.to_json import *
import io


def parse_text_to_dict(text):
    lines = text.strip().split("\n")
    data = {}
    current = data
    stack = []
    append_bytes_next_line = False

    for line in lines:
        if 'b = msg:' in line:
            key = re.search('\d+', line).group()
            new_data = {}
            current[key] = new_data
            stack.append(current)
            current = new_data
        elif 'b = bytes' in line:
            key, value = re.findall('\d+', line)[:2]
            append_bytes_next_line = True
        elif append_bytes_next_line:
            current[key] = ' '.join(re.findall('([A-Fa-f0-9]{2})', line))
            append_bytes_next_line = False
        elif 'i =' in line:
            key, value = re.findall('\d+', line)[:2]
            current[key] = int(value)
        elif '}' in line:
            current = stack.pop()

    return data


parser = StandardParser()
fh = bytes.fromhex('088d111001180022230a2108bf9eb3fd0210001a173805c20112e593aae9878ce79c8be588b0e79a84efbc9f')
file_obj = io.BytesIO(fh)
output = parser.parse_message(file_obj, "message")
print(output)
data = parse_text_to_dict(output)
print(json.dumps(data, indent=4))
