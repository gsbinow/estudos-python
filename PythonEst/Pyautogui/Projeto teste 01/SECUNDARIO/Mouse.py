from pynput import mouse

contador = 0
print('--- Mapeador de clique! ----')

def ao_clicar(x, y, botão, pressionado):
    global contador # Para contar os cliques
    if pressionado:
        if botão== mouse.Button.middle: #Para encerrar com o botao do meio do mouse
            print('\n---Mapeamento encerrado---')
            return False
        
        contador += 1
        print(f'CLique nº {contador} | Posição: X = {x}, Y = {y} | Botão = {botão}')
        print(f'{x,y}')
        print(f'{botão}')

with mouse.Listener(on_click=ao_clicar) as ouvinte:
    ouvinte.join()