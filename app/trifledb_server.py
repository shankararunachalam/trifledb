import asyncio
import argparse
from trifledb import TrifleDB

trifledb = TrifleDB()

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

async def main(host, port):
    server = await asyncio.start_server(
        serve, host, port)

    async with server:
        await server.serve_forever()

parser = argparse.ArgumentParser(description='trifledb asyncio server')
parser.add_argument('-i', '--host', help='host name or ip address where the server will run', default='127.0.0.1')
parser.add_argument('-p', '--port', help='port on which the server will listen', default=6789)
args = parser.parse_args()
asyncio.run(main(args.host, args.port))