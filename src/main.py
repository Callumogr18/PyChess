import pygame
import sys
from const import *
from game import Game


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")
        self.game = Game()

    def mainloop(self):
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            # Displays the chessboard
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)  # Show all pieces except the dragged one

            for event in pygame.event.get():

                # Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.calc_moves(piece, clicked_row, clicked_col)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)

                # Mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)

                # Click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                # Quit game
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if dragger.dragging:
                dragger.update_blit(screen)  # Ensure dragged piece is drawn on top

            pygame.display.update()


main = Main()
main.mainloop()
