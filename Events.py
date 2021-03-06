import pygame
import sys
from pygame.locals import *

class Events():
    """Listens for User Input"""
    def  __init__(this):
        this.leftClick = False
        this.left = False
        this.right = False
        this.up = False
        this.down = False
        this.key = 0

    def Update(this):
        this.key = -1
        this.backspace = 0
        for event in pygame.event.get(): # Checks each event
            if (event.type == QUIT): # Application closed
                sys.exit(0)

            if (event.type == MOUSEBUTTONDOWN): # Left mouse click
                this.leftClick = True

            elif (event.type == MOUSEBUTTONUP): # Right mouse clicks
                this.leftClick = False

            if (event.type == KEYDOWN):
                this.key = event
                if (event.key == K_LEFT):
                    this.left = True
                elif (event.key == K_RIGHT):
                    this.right = True
                elif (event.key == K_UP):
                    this.up = True
                elif (event.key == K_DOWN):
                    this.down = True

            if (event.type == KEYUP):
                if (event.key == K_LEFT):
                    this.left = False
                elif (event.key == K_RIGHT):
                    this.right = False
                elif (event.key == K_UP):
                    this.up = False
                elif (event.key == K_DOWN):
                    this.down = False

    def GetMouseDown(this):
        return this.leftClick

    def GetHorizontal(this):
        if (this.left == this.right):
            return 0
        elif (this.left):
            return -1
        else:
            return 1

    def GetVertical(this):
        if (this.up == this.down):
            return 0
        elif (this.up):
            return -1
        else:
            return 1

    def GetKey(this):
        return this.key;