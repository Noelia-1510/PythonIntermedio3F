import numpy as np
import pygame
import sys
import math

FILA = 6
COLUMNA = 7

AZUL = (0, 76, 153)
NEGRO = (0,0,0)
AMARILLO = (255, 255, 0)
ROJO = (255,0,0)
NARANJA = (255, 135, 0)

pygame.font.init()
MY_FUENTE = pygame.font.SysFont("Arial", 75)

TAMANIOCAJA = 75
ancho = COLUMNA * TAMANIOCAJA
alto = (FILA + 1) * TAMANIOCAJA
tamanio = (ancho,alto)
RADIO = int(TAMANIOCAJA/2-5)

def crear_tablero():
    board = np.zeros((FILA,COLUMNA))
    return board

def lugar_valida(board,col):
    return board[FILA-1][col] == 0

def obtener_siguiente_fila_disponible(board, col):
    for f in range(FILA):
        if board[f][col] == 0:
            return f

def soltar_pieza(board, row, col, piece):
    board[row][col] = piece

def mostrar_tablero(board):
    print(np.flipud(board))


tablero = crear_tablero()
game_over = False
turno = 0

def es_ganador(board, piece):
    #revisamos horizontal
    for c in range(COLUMNA -3):
        for f in range(FILA):
            if board[f][c] == piece and board[f][c+1] == piece and board[f][c+2] == piece and board[f][c+3] == piece:
                return True
    
    #revisamos vertical
    for c in range(COLUMNA):
        for f in range(FILA -3):
            if board[f][c] == piece and board[f+1][c] == piece and board[f+2][c] == piece and board[f+3][c] == piece:
                return True
    
    # verificando diagonales positivas
    for c in range(COLUMNA-3):
        for r in range(FILA-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True 

    # verificando diagonales negativas
    for c in range(COLUMNA-3):
        for r in range(3, FILA):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True 



def dibujar_tablero(board):
    for c in range(COLUMNA):
        for f in range(FILA):
            pygame.draw.rect(pantalla,AZUL,(c*TAMANIOCAJA, f*TAMANIOCAJA+TAMANIOCAJA,TAMANIOCAJA,TAMANIOCAJA))
            pygame.draw.circle(pantalla,NEGRO,(int(c*TAMANIOCAJA+TAMANIOCAJA/2),int(f*TAMANIOCAJA+TAMANIOCAJA+TAMANIOCAJA/2)),RADIO)
        
    for c in range(COLUMNA):
        for f in range(FILA):
            if board[f][c] == 1:
                pygame.draw.circle(pantalla,AMARILLO,(int(c*TAMANIOCAJA+TAMANIOCAJA/2),(alto + TAMANIOCAJA)- int(f*TAMANIOCAJA+TAMANIOCAJA+TAMANIOCAJA/2)), RADIO)
            elif board[f][c] == 2:
                pygame.draw.circle(pantalla,ROJO,(int(c*TAMANIOCAJA+TAMANIOCAJA/2),(alto + TAMANIOCAJA)- int(f*TAMANIOCAJA+TAMANIOCAJA+TAMANIOCAJA/2)), RADIO)
    
    pygame.display.update()

pygame.init()

pantalla  = pygame.display.set_mode(tamanio)

dibujar_tablero(tablero)
#pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(pantalla, NEGRO, (0,0, ancho,TAMANIOCAJA))
            posx = event.pos[0]
            if turno == 0:
                pygame.draw.circle(pantalla, AMARILLO, (posx, int(TAMANIOCAJA/2)), RADIO)
            else: 
                pygame.draw.circle(pantalla, ROJO, (posx, int(TAMANIOCAJA/2)), RADIO) 
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(pantalla, NEGRO, (0,0, ancho, TAMANIOCAJA))
            
            #solicitando la movida al jugador 1
            if turno == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/TAMANIOCAJA))
                
                if lugar_valida(tablero, col):
                    row = obtener_siguiente_fila_disponible(tablero, col)
                    soltar_pieza(tablero, row, col, 1)
                    
                    if es_ganador(tablero, 1):
                        label = MY_FUENTE.render("Jugador 1 Gana!!!", 1, NARANJA)
                        pantalla.blit(label, (40,10))
                        game_over = True
            #solicitando la movida al jugador 2
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/TAMANIOCAJA))

                if lugar_valida(tablero, col):
                    row = obtener_siguiente_fila_disponible(tablero, col)
                    soltar_pieza(tablero, row, col, 2)

                    if es_ganador(tablero, 2):
                        label = MY_FUENTE.render("Jugador 2 Gana!!!", 1, NARANJA)
                        pantalla.blit(label, (40,10))
                        game_over = True


            dibujar_tablero(tablero)
            turno += 1
            turno = turno %2

            if game_over:
                pygame.time.wait(5000)
