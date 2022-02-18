import os
import shutil

from conans import ConanFile


class MidRight(ConanFile):
    name = "mid_right"
    version = "1.0.0"
    license = ".."
    
    settings = 'os'
    requires = ['lower/1.0.0@_/_']
    
    exports_sources = ['readme.txt']
    
    def configure(self):
        self.options["lower"].my_option = 'b'
    
    def build(self):
        pass

    def package(self):
        self.copy('readme.txt')
