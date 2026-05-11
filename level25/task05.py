import asyncio

async def main():
    print("Início")
    await asyncio.sleep(3)
    print("Em progresso")
    await asyncio.sleep(2)
    print("Fim")

asyncio.run(main())