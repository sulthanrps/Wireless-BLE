import asyncio
from bleak import BleakScanner

async def scan_devices():
    devices = await BleakScanner.discover()
    print(f"Ditemukan {len(devices)} perangkat")
    for device in devices:
        print(f"MAC Address: {device.address} | Nama Device : {device.name}")

asyncio.run(scan_devices())