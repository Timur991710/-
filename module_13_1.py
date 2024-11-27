import  asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    sle_ep = 10 / power
    for i in range(5):
        await asyncio.sleep(sle_ep)
        i+=1
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    silach_1 = asyncio.create_task(start_strongman('Pasha', 3))
    silach_2 = asyncio.create_task(start_strongman('Denis', 6))
    silach_3 = asyncio.create_task(start_strongman('Apollon', 10))
    await  silach_1
    await silach_2
    await  silach_3

asyncio.run(start_tournament())