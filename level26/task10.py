import asyncio

async def task(n):
    await asyncio.sleep(2)
    print(f"Task {n} done")

async def main():
    tasks = [task(i) for i in range(1, 31)]
    await asyncio.gather(*tasks)

asyncio.run(main())