import asyncio

async def set_future_exception(future):
    await asyncio.sleep(2)
    future.set_exception(Exception("An error has occurred"))

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    
    asyncio.create_task(set_future_exception(future))

    try:
        await future
    except Exception as e:
        print(f"Exception occurred: {e}")

asyncio.run(main())