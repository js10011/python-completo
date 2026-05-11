import asyncio

async def async_function_1():
    print("Início async_function_1")
    await asyncio.sleep(2)
    print("Conclusão async_function_1")

async def async_function_2():
    print("Início async_function_2")
    await asyncio.sleep(1)
    print("Conclusão async_function_2")

async def main():
    print("Início main")
    task1 = asyncio.create_task(async_function_1())
    task2 = asyncio.create_task(async_function_2())
    
    await task1
    await task2
    print("Conclusão main")

asyncio.run(main())