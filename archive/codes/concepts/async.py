import asyncio





async def task(name, time_taken):
    print(f"Starting {name}")
    await asyncio.sleep(time_taken)
    print(f"Completed {name}")

async def main():
    await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 5),
        task("Task 3", 1)
    )

asyncio.run(main())


#####
import asyncio

async def task1():
    print("कार्य 1 शुरू हो रहा है...")
    await asyncio.sleep(2)
    print("कार्य 1 समाप्त!")

async def task2():
    print("कार्य 2 शुरू हो रहा है...")
    await asyncio.sleep(1)
    print("कार्य 2 समाप्त!")

async def main():
    await asyncio.gather(task1(), task2())  # दोनों कार्य साथ चलेंगे

asyncio.run(main())