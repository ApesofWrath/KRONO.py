import math
from constants import Drive as k
from constants import unit

import wpilib
import wpimath.kinematics
import wpimath.geometry
import wpimath.controller
import wpimath.trajectory

from rev import CANSparkMax, CANEncoder

# https://github.com/ApesofWrath/2024-mentor-summer/blob/master/subsystems/drive/swervemodule.py