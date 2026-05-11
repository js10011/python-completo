import asyncio

class AsyncIterator:
    def __init__(self):
        self.current = 1

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current > 5:
            raise StopAsyncIteration
        await asyncio.sleep(1)
        value = self.current
        self.current += 1
        return value

async def main():
    async for number in AsyncIterator():
        print(number)

asyncio.run(main())