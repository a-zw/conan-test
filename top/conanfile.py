import os
import shutil

from conans import ConanFile


class Top(ConanFile):
    name = "top"
    version = "1.0.0"
    license = ".."
    
    settings = 'os'
    requires = ['mid_left/1.0.0@_/_', 'mid_right/1.0.0@_/_']
    
    exports_sources = ['readme.txt']

    def build(self):
        pass

    def package(self):
        self.copy('readme.txt')


