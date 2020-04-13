import pygame, random
from pygame.locals import *

def on_grid_random(): #Função p/ criar a maça em posição inteira
	x = random.randint(0,590)
	y = random.randint(0,590)
	return (x//10 * 10, y//10 * 10 )

def collision(c1, c2): #função de colisão para maça e snake
	return (c1[0] == c2[0]) and (c1[1] == c2[1] )

pygame.init() #Iniciando game
screen = pygame.display.set_mode((600,600)) #Criando display do jogo
pygame.display.set_caption('Snake') #Nome de titulo

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = [(200,200), (210, 200), (220,200)] #Config da Snake em lista
snake_skin = pygame.Surface((10,10)) #Tamanho do corpo
snake_skin.fill((255,255,255)) #Cor branca(pode usar spryte e por imagem)

apple_pos = on_grid_random() #Posição da maça
apple = pygame.Surface((10,10)) #Config da maça
apple.fill((255,0,0)) #Vermelho

my_direction = LEFT

clock = pygame.time.Clock() #Objeto para reduzir o fps da snake

#Padrao de jogos rodar em loop infinito
while True:
	clock.tick(20)
	for event in pygame.event.get(): #Evento para fechar o jogo
		if event.type == QUIT:
			pygame.quit()

		if event.type == KEYDOWN: #DIreção da cabeça da snake controlada pelo usuario
			if event.key == K_UP:
				my_direction = UP
			if event.key == K_DOWN:
				my_direction = DOWN
			if event.key == K_LEFT:
				my_direction = LEFT
			if event.key == K_RIGHT:
				my_direction = RIGHT

	if collision(snake[0], apple_pos):#função p/ comparar posição entre a maçã e a snake e aumentar a snake
		apple_pos = on_grid_random()
		snake.append((0,0))

	for i in range(len(snake) - 1, 0, -1): #Faz o corpo da snake acompanhar a cabeça
		snake[i] = (snake[i-1][0], snake[i-1][1])

	if my_direction == UP: #Direção da cebeça da snake
		snake[0] = (snake[0][0], snake[0][1] - 10)
	if my_direction == DOWN:
		snake[0] = (snake[0][0], snake[0][1] + 10)
	if my_direction == RIGHT:
		snake[0] = (snake[0][0] + 10, snake[0][1])
	if my_direction == LEFT:
		snake[0] = (snake[0][0] - 10, snake[0][1])

	screen.fill((0,0,0)) #Limpar a tela varias vezes por segundo
	screen.blit(apple, apple_pos) #Plotando a maça
	for pos in snake: #Plotando a snake em cada posição
		screen.blit(snake_skin, pos)

	pygame.display.update()