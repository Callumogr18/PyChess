import pygame
from const import *
from board import Board
from dragger import Dragger


class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    # Show methods
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) # Light green
                else:
                    color = (119, 154, 88) # Dark green
                rect = (col * SQSIZE, row * SQSIZE, WIDTH, HEIGHT)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # Check for piece on the board
                """
                1. Checking if square has a piece
                2. Saving that piece in a variable
                3. Taking the image of the piece
                4. Center the image
                5. The texture_rect is going to be
                   the image we created, but centered
                6. Blit the image inside texture_rect
                """
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        # Center img on x-axis
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            for move in piece.moves:
                """
                1. Create colour to blit it
                2. Create rect
                3. Blit it 
                """
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)