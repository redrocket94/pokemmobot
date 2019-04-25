import GameLoader, ScreenGrabber
import time

game = GameLoader.GameLoader("C:\\Users\\Oliver\\AppData\\Roaming\\PokeMMO")
scrGrab = ScreenGrabber.ScreenGrabber()
game.StartGame()
time.sleep(5)
game.GetAllPIDs()
time.sleep(1)
while True:
    scrGrab.CaptureImg(dimensions=game.GetWindowCoords())