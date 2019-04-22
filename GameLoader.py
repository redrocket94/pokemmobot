import pywinauto
import os
import time
import re
import logging
"""
    Class for mainly interacting with the game client in ways that are fundamental to the stability and
    operability of the bot, by ensuring the game is active and stable.
    This class also provides a host of functionality that allows for the user to request information about the
    current process and its specificities.
    """

class GameLoader:

    # directory var declared
    directory = ""
    originalDirectory = os.getcwd()

    # TODO Make instances self-regulating list
    # game & game_wrapper vars declared
    game = None
    game_wrapped = None

    # logger var declared & LOG_FORMAT set
    logger = None
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"


    # Initialization of game instance
    def __init__(self, directory):
        self.directory = directory
        os.chdir(self.directory)
        logging.basicConfig(filename=(self.originalDirectory + "\\log"),
                            level=logging.DEBUG,
                            format=self.LOG_FORMAT,
                            filemode="w")
        self.logger = logging.getLogger()

    # Function to print to console and store in log same message
    # TODO optimize with logging module
    def _PrintAndLog(self, message):
        print(message)
        self.logger.debug(message)


    # Function to start game, connect and wrap
    def StartGame(self, instance_num=0):
        try:
            self._PrintAndLog("Starting game...")
            pywinauto.Application(backend="uia").start("PokeMMO.exe")

            time.sleep(3)
            self._PrintAndLog("Game started!")

            self._PrintAndLog("Connecting to game...")
            self.game = pywinauto.Application().connect(title="PokeMMO", found_index=instance_num)
            self._PrintAndLog("Connected!")

            self._PrintAndLog("Wrapping game...")
            self.game_wrapped = self.game.window().wrapper_object()
            self._PrintAndLog("Game wrapped!")
        except Exception as e:
            self._PrintAndLog("Could not start game! Shutting down...")
            self.logger.error(e)
            exit()


    # Function to get PIDs of all PokeMMO instances (for future use)
    def GetAllPIDs(self):
        try:
            for process in pywinauto.application.process_get_modules():
                for el in process:
                    if ("PokeMMO" in str(el)):
                        # TODO add real functionality
                        print(process)
        except Exception as e:
            self._PrintAndLog("Error occurred, was unable to retrieve PID list for all processes!")
            self.logger.error(e)


    # Function to find and connect to first instance (default) of PokeMMO found
    def ConnectGame(self, instance_num=0):
        try:
            self._PrintAndLog("Connecting to game...")
            self.game = pywinauto.Application().connect(title="PokeMMO", found_index=instance_num)

            self._PrintAndLog("Wrapping game...")
            self.game_wrapped = self.game.window().wrapper_object()

            self._PrintAndLog("Success!")
        except Exception as e:
            self._PrintAndLog("Error has occured, shutting down...")
            self.logger.error(e)
            exit()


    # Function to get screen dimensions/coordinates of game instance
    def GetWindowCoords(self):
        try:
            # TODO Function too long, probably faster way to do this
            coordsStr = str(self.game_wrapped.rectangle())
            coordsList = coordsStr.split(",")
            for i in range(4):
                coordsList[i] = int(re.sub(r"\D", "", coordsList[i]))
            return coordsList
        except Exception as e:
            self._PrintAndLog("Failed returning window coords!")
            self.logger.error(e)
            exit()