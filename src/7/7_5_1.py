import asyncio

async def async_task(n):
    print(f"Start task {n}")
    await asyncio.sleep(1)
    print(f"End task {n}")

async def main():
    await asyncio.gather(
        async_task(1),
        async_task(2),
        async_task(3)
    )

asyncio.run(main())