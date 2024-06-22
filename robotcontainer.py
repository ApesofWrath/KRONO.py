import wpilib
import commands2

class RobotContainer:
	def __init__(self, isReal=True):
		# TODO: subsystems
		self.robotDrive = None
		self.configureButtonBindings()
		self.driverController = wpilib.XboxController(0)
		# TODO: robotDrive.setDefaultCommand

	def configureButtonBindings(seld) -> None:
		pass

	def getAutonomousCommand(self) -> commands2.Command:
		return commands2.InstantCommand()