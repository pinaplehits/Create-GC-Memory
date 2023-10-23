import os
import shutil

# Get the current directory and add games directory
games_dir = os.path.join(os.getcwd(), "games")

# Get all the directories in the current directory
directories = [
    d for d in os.listdir(games_dir) if os.path.isdir(os.path.join(games_dir, d))
]

# Create a new list using the 4 characters after '['
games_id = [d[d.index("[") + 1 : d.index("[") + 5] for d in directories]

# Loop through each game id
for game_id in games_id:
    # Define the source and destination paths
    source_path = os.path.join(os.getcwd(), "CHANGE_TO_ID.raw")
    destination_path = os.path.join(os.getcwd(), "saves", f"{game_id}.raw")

    # Check if the file already exists in the saves folder
    if not os.path.exists(destination_path):
        # Duplicate the file and rename it to the game id
        shutil.copy(source_path, destination_path)
