import commands2
import robot_container
import wpilib
import wpilib.drive


class Robot(commands2.TimedCommandRobot):
	def robotInit(self):
		self.container = robot_container.RobotContainer(isReal=self.isReal())

	def autonomousInit(self):
		pass

	def autonomousPeriodic(self):
		pass

	def teleopInit(self):
		pass

	def teleopPeriodic(self):
		pass

	def testInit(self):
		pass

	def testPeriodic(self):
		pass

	def robotPeriodic(self):
		pass
