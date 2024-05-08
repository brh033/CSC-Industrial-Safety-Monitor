import sys
import pygame
import random
import gasReading  # Import the gasReading module
from pygame.locals import *
import radiationReading

class PipBoyGUI:
    def __init__(self, display_size=(800, 600), box_size=(500, 300)):
        pygame.init()
        self.screen = pygame.display.set_mode(display_size)
        pygame.display.set_caption('Fallout Pip-Boy GUI')
        self.clock = pygame.time.Clock()


        self.font = pygame.font.Font(None, 26)  # Using default font

        # Define colors
        self.background_color = (12, 27, 10)  # Hex: 0c1b0a
        self.font_color = (143, 248, 87)      # Hex: 8ff857

        # Load and resize image
        self.image = pygame.image.load("images/pipboy.png")
        self.image = pygame.transform.scale(self.image, (200, 200))  # Adjust size as needed

        # Define button properties
        self.button_width = 300
        self.button_height = 50
        self.button_color = (50, 50, 50)
        self.button_hover_color = (100, 100, 100)
        self.button_font = pygame.font.Font(None, 30)

        # Button positions
        self.button_positions = [(50, 10), (470, 10)]

        # Button labels
        self.button_labels = ["Gas Info", "Radiation Reading"]

        # Box properties
        self.box_rect = pygame.Rect((display_size[0] - box_size[0]-250) // 2, (display_size[1] - box_size[1]) // 2, *box_size)

    def run(self):
        running = True
        geiger_counter = radiationReading.get_cpm()
        while running:
            self.screen.fill(self.background_color)  # Set background color
            
            # Draw the lined box around the display area
            pygame.draw.rect(self.screen, (255, 255, 255), self.box_rect, 3)  # White rectangle with a thickness of 3 pixels

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        # Check if any button is clicked
                        for i, pos in enumerate(self.button_positions):
                            if pos[0] <= event.pos[0] <= pos[0] + self.button_width and \
                               pos[1] <= event.pos[1] <= pos[1] + self.button_height:
                                # Call function based on the button clicked
                                if i == 0:
                                    self.open_window1()
                                elif i == 1:
                                    self.open_window2(geiger_counter)

            # Simulated Geiger counter
            # geiger_counter += random.randint(0, 5)  # Simulated increase in counts per minute
            if geiger_counter > 1000:  # Reset if it goes too high
                geiger_counter = 0

            #Display air quality status
            gas_level = gasReading.readadc(gasReading.MQ2_APIN, gasReading.SPICLK, gasReading.SPIMOSI, gasReading.SPIMISO, gasReading.SPICS)
            air_quality = (gas_level / 1024.) * 3.3
            # air_quality = random.uniform(0, 2)#test
            if air_quality > 1.5:
                self.display_text(f"Gas Leakage !!!",(50,200))
                
            self.display_text(f"Gas AD value = {air_quality}",(50,230))


            middle_y = self.box_rect.centery

            # Drawing a dotted line in the middle
            dash_length = 10
            for x in range(self.box_rect.left, self.box_rect.right, dash_length * 2):
                pygame.draw.line(self.screen, (255, 255, 255), (x, middle_y), (x + dash_length, middle_y), 3)

            # Display Geiger counter status
            if geiger_counter > 150:
                self.display_text(f"Alert!!!! Hazardious Radiation", (50, 300))
                self.display_text(f'Geiger Counter: {geiger_counter} CPM', (50, 350))
            elif 50 <= geiger_counter <= 150:
                self.display_text(f"Radiation detected! ", (50, 300))
                self.display_text(f'Geiger Counter: {geiger_counter} CPM', (50, 350))
            else:
                self.display_text(f'Geiger Counter: {geiger_counter} CPM', (50, 300))

            # Display image
            self.screen.blit(self.image, (600, 390))

            # Draw buttons
            for i, (x, y) in enumerate(self.button_positions):
                color = self.button_color
                if x <= pygame.mouse.get_pos()[0] <= x + self.button_width and \
                   y <= pygame.mouse.get_pos()[1] <= y + self.button_height:
                    color = self.button_hover_color
                pygame.draw.rect(self.screen, color, (x, y, self.button_width, self.button_height))
                text = self.button_font.render(self.button_labels[i], True, self.font_color)
                self.screen.blit(text, (x + 10, y + 10))

            pygame.display.flip()
            self.clock.tick(30)
        
        pygame.quit()

        

    def display_text(self, text, pos):
        text_surface = self.font.render(text, True, self.font_color)
        self.screen.blit(text_surface, pos)

    def open_window1(self):
        gas_window = GasInfoWindow()
        gas_window.run()

    def open_window2(self, geiger_counter):
        # Implement window 2 logic here
        window2 = Window2(self, geiger_counter)
        window2.run()

class GasInfoWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Gas Info')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)  # Using default font
        self.return_button = pygame.Rect(300, 300, 200, 70)  # Increase size of return button
        self.return_label = "Return"
        # Define colors
        self.background_color = (12, 27, 10)  # Hex: 0c1b0a
        self.font_color = (143, 248, 87)      # Hex: 8ff857

    def run(self):
        running = True
        while running:
            self.screen.fill(self.background_color)  # Fill with background color

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.return_button.collidepoint(event.pos):
                            return  # Return to main menu

            # Simulated sensor readings
            gas_level = gasReading.readadc(gasReading.MQ2_APIN, gasReading.SPICLK, gasReading.SPIMOSI, gasReading.SPIMISO, gasReading.SPICS)
            air_quality = (gas_level / 1024.) * 3.3

            #Display info
            text1 = self.font.render(f'Gas level: {gas_level}', True, self.font_color)
            text2 = self.font.render(f' Air quality: {ai_qualityr} ', True, self.font_color)
            self.screen.blit(text12, (50, 50))
            self.screen.blit(text, (50, 100))
            
            # Draw other elements and text here

            pygame.draw.rect(self.screen, (100, 100, 100), self.return_button)  # Draw return button
            return_text = self.font.render(self.return_label, True, self.font_color)
            self.screen.blit(return_text, (self.return_button.x + 50, self.return_button.y + 20))  # Adjust label position

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

    # Add display_text method here


class Window2:
    def __init__(self, pipboy, geiger_counter):
        pygame.init()
        self.pipboy = pipboy
        self.geiger_counter = geiger_counter
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Window 2')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)  # Using default font
        self.return_button = pygame.Rect(300, 300, 200, 70)  # Increase size of return button
        self.return_label = "Return"
        # Define colors
        self.background_color = (12, 27, 10)  # Hex: 0c1b0a
        self.font_color = (143, 248, 87)      # Hex: 8ff857

    def run(self):
        running = True
        while running:
            self.screen.fill(self.background_color)  # Fill with background color

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.return_button.collidepoint(event.pos):
                            running = False  # Exit Window 2 and return to Window 1

            # display text

            text = self.font.render(f'Geiger Counter: {self.geiger_counter} CPM', True, self.font_color)
            self.screen.blit(text, (50, 50))

            
            # Draw other elements and text here
            pygame.draw.rect(self.screen, (100, 100, 100), self.return_button)  # Draw return button
            return_text = self.font.render(self.return_label, True, self.font_color)
            self.screen.blit(return_text, (self.return_button.x + 40, self.return_button.y+10))  # Adjust label position

            pygame.display.flip()
            self.clock.tick(30)

        # After exiting Window 2, resume Window 1
        self.pipboy.run()

    # Add display_text method here



if __name__ == '__main__':
    pipboy = PipBoyGUI()
    pipboy.run()
    
    # pygame.quit()
    # sys.exit()
