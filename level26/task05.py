import asyncio

class AsyncContextManager:
    async def __aenter__(self):
        print("Entrando no contexto")
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Saindo do contexto")

    async def do_work(self):
        await asyncio.sleep(2)
        print("Dentro do contexto")

async def main():
    async with AsyncContextManager() as manager:
        await manager.do_work()

asyncio.run(main())