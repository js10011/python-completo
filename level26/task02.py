import asyncio

async def long_running_task():
    try:
        print("Task started, will sleep for 5 seconds...")
        await asyncio.sleep(5)
        print("Task completed!")
    except asyncio.CancelledError:
        print("Task was cancelled.")

async def main():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Caught task cancellation.")

asyncio.run(main())