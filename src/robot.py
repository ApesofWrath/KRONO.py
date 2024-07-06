import commands2
import wpilib
import wpilib.drive
from robot_container import RobotContainer

# I've put all the documented methods in the robot class so that they are easier
# to find as we replicate the codebase, but they can be removed when known to be
# unnecessary
# -Toryn


class Robot(commands2.TimedCommandRobot):
	# * Main
	def robotInit(self) -> None:
		self.scheduler = commands2.CommandScheduler.getInstance()
		self.container = RobotContainer(isReal=self.isReal())

	def robotPeriodic(self) -> None:
		self.scheduler.run()

	# * Autonomous
	def autonomousInit(self) -> None:
		pass

	def autonomousPeriodic(self) -> None:
		pass

	def autonomousExit(self) -> None:
		pass

	# * Disabled
	def disabledInit(self) -> None:
		pass

	def disabledPeriodic(self) -> None:
		pass

	def disabledExit(self) -> None:
		pass

	# * Teleop
	def teleopInit(self) -> None:
		pass

	def teleopPeriodic(self) -> None:
		pass

	def teleopExit(self) -> None:
		pass

	# * Test
	def testInit(self) -> None:
		pass

	def testPeriodic(self) -> None:
		pass

	def testExit(self) -> None:
		pass

	# * Misc
	def driverStationConnected(self) -> None:
		pass
