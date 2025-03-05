import socket
import struct

can_frame_fmt = "=IB3x8s"
can_frame_size = struct.calcsize(can_frame_fmt)

def build_can_frame(can_id, data):
    can_dlc = len(data)
    data = data.ljust(8, b'\x00')
    return struct.pack(can_frame_fmt, can_id, can_dlc, data)

def dissect_can_frame(frame):
    can_id, can_dlc, data = struct.unpack(can_frame_fmt, frame)
    return (can_id, can_dlc, list(data[:can_dlc]))

s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('vcan0',))
s.send(build_can_frame(0x100, b'\x01\x02\x03\x04'))

frame, addr = s.recvfrom(can_frame_size)
id, dlc, data = dissect_can_frame( frame)

print("Received", id, dlc, data)

s.close()
