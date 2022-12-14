# Bluetooth device name: "YONGNUO LED"
deviceUUID = "5D21F383-857D-F3E3-2F08-8C080C6835F2"  
primaryServiceUuid = 'f000aa60-0451-4000-b000-000000000000'
receiveCharUuid = 'f000aa63-0451-4000-b000-000000000000'
sendCharUuid = 'f000aa61-0451-4000-b000-000000000000'

# connect to LED bluetooth light
import asyncio
import sys
from bleak import BleakClient

LED_r = int(sys.argv[1]) # warm value 0-99
LED_g = int(sys.argv[2]) # warm value 0-99
LED_b = int(sys.argv[3]) # warm value 0-99

async def main():
    async with BleakClient(deviceUUID) as client:
        # Read a characteristic, etc.
        await client.write_gatt_char(sendCharUuid, bytearray([0xae,0xa1,LED_r,LED_g,LED_b,0x56]), response=True)

asyncio.run(main())