import pygame

WIDTH = 360
HEIGHT = 700
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # создаем экземпляр класса экран
pygame.display.set_caption("Flappy bird")
clock = pygame.time.Clock() #  отсчеты времени (FPS)

bg = pygame.image.load("img/bg.png") # изображение фона
ground = pygame.image.load("img/ground.png") # изображение земли
ground_x = 0


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f"img/bird{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        # self.velocity = 0.1
    def update(self):
        self.counter = self.counter + 1
        # self.counter += 1
        self.bird_time = 20
        if self.counter > self.bird_time:
            self.counter = 0
            self.index += 1
            if self.index > 2:
                self.index = 0
        self.image = self.images[self.index]
        # self.velocity += 0.2
        # self.rect.y += self.velocity
        self.rect.y += 1
        if self.rect.y > 564:
            # self.velocity = 0
            self.rect.y = 564

bird_group = pygame.sprite.Group()
flappy1 = Bird(90, HEIGHT // 2)
# flappy1 = Bird(90, 390)

bird_group.add(flappy1)
running = True
while running:
    'Игровой цикл'
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ground_x = ground_x - 1
    # ground_x -= 1
    if ground_x <= -500:
        ground_x = 0

    screen.blit(bg, (0, 0)) # отрисовка изображение
    bird_group.draw(screen)
    bird_group.update()
    screen.blit(ground, (ground_x, 600))
    pygame.display.flip() # обновление экрана

pygame.quit()
