from enum import Enum

import commands2
import navx
import wpilib


class Speed(Enum):
	SLOW = 0.5
	NORMAL = 1.0


class Drivetrain(commands2.Subsystem):
	def __init__(self) -> None:
		self.speedFactor = 1.0
		self.navx = navx.AHRS.create_spi(wpilib.SPI.Port.kMXP)

	def resetGyro(self) -> None:
		self.navx.zeroYaw()

	def setSpeed(self, speed: Speed) -> None:
		self.speedFactor = speed
