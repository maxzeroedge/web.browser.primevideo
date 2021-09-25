import os, sys, platform
import src.install_required as installer
cef = None # Dynamic Import

class PrimeVideoBrowser:
    def __init__(self):
        cefpython3 = __import__('cefpython3')
        cef = cefpython3.cefpython
        sys.excepthook = cef.ExceptHook
        cef.Initialize()
        self.browser = cef.CreateBrowserSync(
            url = 'https://primevideo.com', 
            window_title='Amazon Prime Video'
        )
        cef.MessageLoop()
        cef.Shutdown()

if __name__ == "__main__":
    installer.update_requirements()
    # importlib.import_module('cefpython3')
    PrimeVideoBrowser()