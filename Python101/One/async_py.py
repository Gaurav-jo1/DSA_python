import random
import asyncio


async def function_1(name):
    random_num = random.uniform(1, 10)
    print(f"Hello {name.capitalize()}, please wait for {int(random_num)} seconds.")
    await asyncio.sleep(random_num)
    print(f"Thanks for waiting {name.capitalize()}")


async def main():
    tasks = [function_1("gaurav"), function_1("elon"), function_1("X")]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
