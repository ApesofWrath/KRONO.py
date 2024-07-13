import commands2
import wpilib
import constants as k

class RobotContainer:
	def __init__(self, isReal=True):
		# TODO: subsystems
		self.robotDrive = None
		self.configureButtonBindings()
		
		self.driverController = wpilib.XboxController(k.driverControllerPort)
		self.operatorController = wpilib.XboxController(k.operatorControllerPort)
		
		# TODO: robotDrive.setDefaultCommand

	def configureButtonBindings(self) -> None:
		pass

	def getAutonomousCommand(self) -> commands2.Command:
		return commands2.InstantCommand()
