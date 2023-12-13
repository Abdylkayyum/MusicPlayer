import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Define function to play music
def play_music(music_file):
    # Check if file exists
    if os.path.isfile(music_file):
        # Load music
        pygame.mixer.music.load(music_file)
        # Play music
        pygame.mixer.music.play()
        # Keep program running until music stops
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print(f"Error: Music file '{music_file}' not found!")

# Define function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Define variable to store music file path
music_file = None

# Prompt user for music file path
music_file = input("Enter the MP3 file path: ")

# Check if music file is entered
if music_file:
    play_music(music_file)
else:
    print("Please enter a valid MP3 file path.")

# Display menu
print("Music Player")
print("1. Play Music")
print("2. Stop Music")
print("3. Exit")

# Get user input
choice = input("> ")

# Handle user choice
if choice == "1":
    play_music(music_file)
elif choice == "2":
    stop_music()
elif choice == "3":
    pygame.quit()
    exit()
else:
    print("Invalid choice!")
