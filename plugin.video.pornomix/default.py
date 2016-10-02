import xbmcaddon

__plugin__ = 'pornomix'
__author__ = 'sfaxman'
__credits__ = 'bootsy'

addon = xbmcaddon.Addon(id='plugin.video.pornomix')
rootDir = addon.getAddonInfo('path')
if rootDir.endswith(';'):
    rootDir = rootDir[:-1]

class Main:
    def __init__(self):
        self.pDialog = None
        self.curr_file = ''
        self.run()

    def run(self):
        import pornomix
        pornomix.Main()

win = Main()
