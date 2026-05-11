import asyncio

async def first_task():
    await asyncio.sleep(1)
    print("Primeira tarefa concluída")

async def second_task():
    await asyncio.sleep(2)
    print("Segunda tarefa concluída")

async def main():
    task1 = asyncio.create_task(first_task())
    task2 = asyncio.create_task(second_task())
    await task1
    await task2

asyncio.run(main())