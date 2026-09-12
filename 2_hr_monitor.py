import asyncio
from bleak import BleakClient

POLAR_MAC_ADDRESS = "20F25B51-96F2-8FC5-A1F6-595F5C4F86CF" 
HR_MEASUREMENT_UUID = "00002a37-0000-1000-8000-00805f9b34fb"
def heart_rate_handler(sender, data):
    bpm = data[1]
    print(f"Denyut Jantung Anda: {bpm} BPM")

async def connect_and_read():
    async with BleakClient(POLAR_MAC_ADDRESS, timeout=60.0) as client:
        print(f"Berhasil Terhubung: {client.is_connected}")
        
        print("Mulai mengambil data detak jantung...")
        await client.start_notify(HR_MEASUREMENT_UUID, heart_rate_handler)
        
        await asyncio.sleep(30)
        
        print("Berhenti mengambil data")
        await client.stop_notify(HR_MEASUREMENT_UUID)

asyncio.run(connect_and_read())