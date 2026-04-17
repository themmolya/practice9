import pygame

class Ball:
    def __init__(self, x, y, radius, speed, width, height):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.width = width
        self.height = height

    def move(self, keys):
        # LEFT
        if keys[pygame.K_LEFT]:
            if self.x - self.radius - self.speed >= 0:
                self.x -= self.speed

        # RIGHT
        if keys[pygame.K_RIGHT]:
            if self.x + self.radius + self.speed <= self.width:
                self.x += self.speed

        # UP
        if keys[pygame.K_UP]:
            if self.y - self.radius - self.speed >= 0:
                self.y -= self.speed

        # DOWN
        if keys[pygame.K_DOWN]:
            if self.y + self.radius + self.speed <= self.height:
                self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)