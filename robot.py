import commands2
import robot_container
import wpilib
import wpilib.drive


class Robot(commands2.TimedCommandRobot):
	def robotInit(self):
		self.container = robot_container.RobotContainer(isReal=self.isReal())
		self.autonomousCommand = self.container.getAutonomousCommand()

	def autonomousInit(self):
		if type(self.autonomousCommand) is commands2.Command:
			self.autonomousCommand.schedule()

	def autonomousPeriodic(self):
		pass

	def teleopInit(self):
		pass

	def teleopPeriodic(self):
		if type(self.autonomousCommand) is commands2.Command:
			self.autonomousCommand.cancel()

	def testInit(self):
		commands2.CommandScheduler.getInstance().cancelAll()

	def testPeriodic(self):
		pass

	def robotPeriodic(self):
		pass
