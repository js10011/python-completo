import asyncio

# Criamos o primeiro loop de eventos
first_event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(first_event_loop)
print("First event loop:", first_event_loop)

# Criamos o segundo loop de eventos
second_event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(second_event_loop)
print("Second event loop:", second_event_loop)