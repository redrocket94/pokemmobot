import GameLoader
import time

game = GameLoader.GameLoader("C:\\Users\\olive\\AppData\\Roaming\\PokeMMO")
game.StartGame()
time.sleep(5)
game.GetAllPIDs()
coords = game.GetWindowCoords()
print(coords)