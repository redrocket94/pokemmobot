import GameLoader
import time

game = GameLoader.GameLoader("C:\\Users\\Oliver\\AppData\\Roaming\\PokeMMO")
game.StartGame()
time.sleep(5)
game.GetAllPIDs()
coords = game.GetWindowCoords()
print(coords)