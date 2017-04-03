#! /usr/bin/python3

from enum import IntEnum

__author__ = "Alena Lifar"
__status__ = "alpha"
__version__ = "0.0.1"

class SerialCommands(IntEnum):
    """
    Serial Commands represent possible numbers to be sent to Arduino Serial Protocol.
    The value represents a decimal integer of proper binary numbers.
    Each digit of a 4-digit binary number represents a direction of movement or turn.
    1 digit: moving forward
    2 digit: moving reverse
    3 digit: turn left
    4 digit: turn right
    """

    def __new__(cls, value, command, description=''):
        obj = int.__new__(cls, value)
        obj._value_ = value

        obj.command = command
        obj.description = description
        return obj

    STOP          = 0,  'Stop',              'Represents binary number: 0000'
    REVERSE       = 4,  'Reverse',           'Represents binary number: 0100'
    REVERSE_RIGHT = 5,  'Reverse and Right', 'Represents binary number: 0101'
    REVERSE_LEFT  = 6,  'Reverse and Left',  'Represents binary number: 0110'
    FORWARD       = 8,  'Forward',           'Represents binary number: 1000'
    FORWARD_RIGHT = 9,  'Forward and Right', 'Represents binary number: 1001'
    FORWARD_LEFT  = 10, 'Forward and Left',  'Represents binary number: 1010'

