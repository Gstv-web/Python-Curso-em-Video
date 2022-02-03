from time import sleep

cont = 0
while True:
    sleep(0.75)
    print(cont)
    if cont == 20:
        break
    cont += 1
print(f'Acabou', end='')