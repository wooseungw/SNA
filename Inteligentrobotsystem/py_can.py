import can

DEV = 'vcan0'
bus = can.interface.Bus(channel=DEV, bustype='socketcan', bitrate=500000)

msg = bus.recv()
print("%s   %X  [%d] "%(DEV, msg.arbitration_id, len(msg.data)), end= ' ')
for n in [d for d in msg.data]:
    print("%02X "%(n), end='')
print()

msg = can.Message(arbitration_id=0x200, data=[0x10, 0x20, 0x30, 0x40], is_extended_id=False)
bus.send(msg)

bus.set_filters([{"can_id": 0x200, "can_mask": 0x7FF, "extended": False}])
msg = bus.recv()
print("%s   %X  [%d] "%(DEV, msg.arbitration_id, len(msg.data)), end= ' ')
for n in [d for d in msg.data]:
    print("%02X "%(n), end='')  
print()
