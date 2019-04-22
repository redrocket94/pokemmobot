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
        try:

            logging.basicConfig(filename=(self.originalDirectory + "\\log"),
                                level=logging.DEBUG,
                                format=self.LOG_FORMAT,
                                filemode="w")
            self.logger = logging.getLogger()

            self._PrintAndLog("Created log in: " + self.originalDirectory)

            self.directory = directory
            os.chdir(self.directory)

        except Exception as e:
            print("ERROR:", e)
            exit()
        finally:
            self._PrintAndLog("Program initialized")

    # Function to print to console and store in log same message as info
    # TODO optimize with logging module
    def _PrintAndLog(self, message, level=20):
        print(message)
        if level is 10:
            self.logger.debug(message)
        elif level is 20:
            self.logger.info(message)
        elif level is 30:
            self.logger.warning(message)
        elif level is 40:
            self.logger.error(message)
        elif level is 50:
            self.logger.critical(message)
        else:
            return


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
            self._PrintAndLog("Could not start game! Shutting down...\n" + e, 50)
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
            self._PrintAndLog("Error occurred, was unable to retrieve PID list for all processes!\n" + e, 40)


    # Function to find and connect to first instance (default) of PokeMMO found
    def ConnectGame(self, instance_num=0):
        try:
            self._PrintAndLog("Connecting to game...")
            self.game = pywinauto.Application().connect(title="PokeMMO", found_index=instance_num)

            self._PrintAndLog("Wrapping game...")
            self.game_wrapped = self.game.window().wrapper_object()

            self._PrintAndLog("Success!")
        except Exception as e:
            self._PrintAndLog("Error has occured, shutting down...", 50)
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
            self._PrintAndLog("Failed returning window coords!\n" + e, 40)
            exit()