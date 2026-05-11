import asyncio

def stop_loop():
    print(f"Status do loop antes de stop: {loop.is_running()}")
    loop.stop()
    print(f"Status do loop depois de stop: {loop.is_running()}")

async def main():
    loop.call_later(3, stop_loop)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()