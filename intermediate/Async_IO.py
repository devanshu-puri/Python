#typical execution flow 

import time
import asyncio

# def func1():
#     time.sleep(3)
#     print("fun 1")

# def func2():
#     time.sleep(3)
#     print( "func 2")

# def func3():
#     time.sleep(3)
#     print("func 3")

# func1()
# func2()
# func3() 


# -----------------------------------------------

# await : to wait for the async function to be completed

# async def func1():
#     time.sleep(3)
#     print("fun 1")

# async def func2():
#     time.sleep(3)
#     print( "func 2")

# async def func3():
#     time.sleep(3)
#     print("func 3")

# async def main():
#     await func1()
#     await func2()
#     await func3() 

# asyncio.run(main())

# ----------------------------------------

async def func1():
    time.sleep(3)
    print("fun 1")

async def func2():
    time.sleep(3)
    print( "func 2")

async def func3():
    time.sleep(3)
    print("func 3")

async def main():
    await func1()
    await func2()
    await func3() 

asyncio.run(main())