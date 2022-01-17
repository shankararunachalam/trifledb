import asyncio
from trifledb import TrifleDB

trifledb = TrifleDB()
loop = asyncio.get_event_loop()

async def process(message):
    args = message.split()
    arg_count = len(args)
    response = 'bad request'
    if arg_count in (2, 3):
        command = args[0]
        key = args[1]
        if command == 'get':
            response = trifledb[key]
            if not response:
                response = 'key not found'
        elif command == 'put' and arg_count == 3:
            value = args[2]
            trifledb[key] = value
            response = 'done'
    return response

async def serve(reader, writer):
    data = await reader.read(100)
    response = await process(data.decode())
    writer.write(response.encode())
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(
        serve, '127.0.0.1', 6789)

    async with server:
        await server.serve_forever()

asyncio.run(main())