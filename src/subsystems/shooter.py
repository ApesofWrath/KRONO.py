from enum import Enum, auto

import commands2
from vision import Vision


class ShooterState(Enum):
	IDLE = auto()
	INTAKING = auto()
	BACKOFF = auto()
	NOTE_FORWARD = auto()
	HOLDING = auto()
	SPINUP = auto()
	SPINUP_PIGEON = auto()
	AMP_BACK = auto()
	AIM_AMP = auto()
	SCORE_AMP = auto()
	RAPID_FIRE = auto()
	FIRE = auto()
	POST_FIRE = auto()
	RAPID_POST_FIRE = auto()
	ZEROING = auto()


class Shooter(commands2.Subsystem):
	def __init__(self) -> None:
		self.state: ShooterState = ShooterState.IDLE
		self.allowSpinup: bool = False

	def activateIntake(self) -> None:
		raise NotImplementedError

	def autoAngle(self, vision: Vision) -> None:
		raise NotImplementedError

	def spinUp(self) -> None:
		raise NotImplementedError

	def atSpeed(self) -> bool:
		raise NotImplementedError
