import subprocess
import uvicorn

import warnings
import asyncio

def run_tests():
    result = subprocess.run(['pytest', 'tests/api_test.py'], capture_output=True, text=True)
    print(result.stdout)  # Вывод результатов тестов
    print(result.stderr)   # Вывод ошибок, если есть


async def uvicorn_start():
    config = uvicorn.Config(
        "src.main:app",
        host='127.0.0.1',
        port='8000'
    )
    server = uvicorn.Server(config)
    await server.serve()

async def runner():
    await asyncio.gather(uvicorn_start())

if __name__ == "__main__":
    run_tests()
    warnings.filterwarnings("ignore")
    asyncio.run(runner())

