import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 800, 600

# Цвета
white = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Поздравление с Днем Рождения! ")

# Определение цветов для салюта
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (128, 0, 128)]


# Определение класса для частиц салюта
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            self.rect.y = 0
            self.rect.x = random.randint(0, width)


# Определение класса для текста "С Днем Рождения!"
class BirthdayText(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        font = pygame.font.Font("RubikBubbles-Regular.ttf", 36)
        self.image = font.render("С Днем Рождения!", True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)


# Группа для хранения всех частиц салюта
all_particles = pygame.sprite.Group()

# Группа для хранения текста
birthday_text = pygame.sprite.GroupSingle(BirthdayText())

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очищаем экран
    screen.fill(white)

    # Генерируем новые частицы
    if random.randint(1, 1) == 1:
        color = random.choice(colors)
        particle = Particle(random.randint(0, width), 0, color)
        all_particles.add(particle)

    # Обновляем и рисуем все частицы
    all_particles.update()
    all_particles.draw(screen)

    # Рисуем текст
    birthday_text.draw(screen)

    # Обновляем экран
    pygame.display.flip()

    # Задержка для анимации
    pygame.time.delay(15)