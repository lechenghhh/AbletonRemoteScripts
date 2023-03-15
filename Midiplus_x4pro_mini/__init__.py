from __future__ import absolute_import, print_function, unicode_literals
from .Midiplus_x4pro_mini import Midiplus_x4pro_mini
import Live 

def create_instance(c_instance):
    u' Creates and returns the Midiplus_x4pro_mini script '
    return Midiplus_x4pro_mini(c_instance)

