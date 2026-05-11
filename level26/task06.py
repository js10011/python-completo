import aiofiles
import asyncio

async def write_to_file(filename):
    async with aiofiles.open(filename, mode='w', encoding='utf-8') as file:
        await file.write("Gravação assíncrona no arquivo")

# Exemplo de uso
async def main():
    await write_to_file("example.txt")

# Executando a função assíncrona
asyncio.run(main())