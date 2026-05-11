import asyncio

async def task1():
    await asyncio.sleep(1)
    return "Resultado da task1"

async def task2():
    await asyncio.sleep(2)
    return "Resultado da task2"

async def main():
    results = await asyncio.gather(task1(), task2())
    print(results)

asyncio.run(main())