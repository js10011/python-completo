import asyncio

async def delayed_print(text, delay):
    await asyncio.sleep(delay)
    print(text)

async def main():
    task1 = asyncio.create_task(delayed_print("Hello after 2 seconds", 2))
    task2 = asyncio.create_task(delayed_print("Hello after 5 seconds", 5))
    await task1
    await task2

asyncio.run(main())