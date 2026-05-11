import asyncio

async def task_one():
    print("Primeira tarefa")
    await asyncio.sleep(2)

async def task_two():
    print("Segunda tarefa")
    await asyncio.sleep(3)

async def main():
    task1 = asyncio.create_task(task_one())
    task2 = asyncio.create_task(task_two())

    await asyncio.gather(task1, task2)

# Iniciando o loop de eventos principal
asyncio.run(main())