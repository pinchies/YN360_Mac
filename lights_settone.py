# Bluetooth device name: "YONGNUO LED"
deviceUUID = "5D21F383-857D-F3E3-2F08-8C080C6835F2"  # you need to use the lights_scanbt.py script to get the correct UUID for your lights.
primaryServiceUuid = 'f000aa60-0451-4000-b000-000000000000'
receiveCharUuid = 'f000aa63-0451-4000-b000-000000000000'
sendCharUuid = 'f000aa61-0451-4000-b000-000000000000'

# connect to LED bluetooth light
import asyncio
import sys
from bleak import BleakClient

LED_warm = int(sys.argv[1]) # warm value 0-255
LED_cool = int(sys.argv[2]) # cold value 0-255

async def main():
    async with BleakClient(deviceUUID) as client:
        # Read a characteristic, etc.
        await client.write_gatt_char(sendCharUuid, bytearray([0xae,0xaa,1,LED_cool,LED_warm,0x56]), response=True)

asyncio.run(main())