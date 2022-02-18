import os
import shutil

from conans import ConanFile


class Lower(ConanFile):
    name = "lower"
    version = "1.0.0"
    license = ".."
    
    settings = 'os'

    options = {'my_option': ['a', 'b']}
    default_options = {'my_option': 'a'}
    
    exports_sources = ['readme.txt']
    
    def build(self):
        pass

    def package(self):
        self.copy('readme.txt')
