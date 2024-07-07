import commands2
import wpilib
from subsystems.climber import Climber
from subsystems.drivetrain import Drivetrain, Speed
from subsystems.led import LED
from subsystems.shooter import Shooter, ShooterState
from subsystems.vision import Vision
from wpimath.filter import Debouncer


class RobotContainer:
	def __init__(self):
		# * Global Class Instances
		self.timer = wpilib.Timer()
		self.scheduler = commands2.CommandScheduler.getInstance()

		# * Subsystems
		self.climber = Climber()
		self.drivetrain = Drivetrain()
		self.led = LED()
		self.shooter = Shooter()
		self.vision = Vision()

		# * Controllers
		self.driverController = wpilib.XboxController(0)
		self.buttonLoop = commands2.CommandScheduler.getDefaultButtonLoop(
			self.scheduler
		)
		self.configureButtonBindings()

		# * Telemetry
		self.chooser = wpilib.SendableChooser()
		self.pathOptions: dict[str, str] = {
			"2NoteCenter": "2NoteCenter",
			"3NoteCenter": "3NoteCenter",
			"2NoteAmpSide": "2NoteAmpSide",
			"3NoteAmpSide": "3NoteAmpSide",
			"4Note": "4Note",
			"Backup": "Backup",
			"Preload": "Preload",
			"PreloadBackupCenter": "PreloadBackupCenter",
			"New Auto": "New Auto",
			"3 Note - test": "3 Note - test",
			"4 Note - test": "4 Note - test",
			"5 Note - test": "5 Note - test",
		}
		self.configureTelemetry()

		self.timer.start()

	def configureTelemetry(self) -> None:
		self.chooser.setDefaultOption("DoNothing", "DoNothing")

		for name, object in self.pathOptions.items():
			self.chooser.addOption(name, object)

		wpilib.SmartDashboard.putData("autoChooser", self.chooser)

	def configureButtonBindings(self) -> None:
		# * Swervedrive zeroing
		self.driverController.start(
			self.buttonLoop,
		).ifHigh(self.drivetrain.resetGyro)

		self.drivetrain.runOnce

		# * Swervedrive slower
		rightBumper = self.driverController.rightBumper(self.buttonLoop)
		# Set to only trigger event when bumper held down for at least 50ms
		# TODO: Adjust debounce time based on real use
		rightBumper.debounce(0.05, Debouncer.DebounceType.kRising).ifHigh(
			lambda: self.drivetrain.setSpeed(Speed.SLOW),
		)
		rightBumper.debounce(0.05, Debouncer.DebounceType.kFalling).ifHigh(
			lambda: self.drivetrain.setSpeed(Speed.NORMAL),
		)

		leftBumper = self.driverController.leftBumper(self.buttonLoop)
		leftBumper.rising().ifHigh(
			lambda: self.drivetrain.setSpeed(Speed.SLOW),
		)
		leftBumper.falling().ifHigh(
			lambda: self.drivetrain.setSpeed(Speed.NORMAL),
		)

		# * Swervedrive Alignment
		# self.driverController.B(self.buttonLoop).ifHigh(
		# 	self.vision.align,
		# )

		# * Shooter
		self.driverController.leftBumper(self.buttonLoop).ifHigh(
			self.shooter.activateIntake
		)
		self.driverController.B(self.buttonLoop).ifHigh(
			lambda: self.shooter.autoAngle(self.vision)
		)
		self.driverController.X(self.buttonLoop).ifHigh(
			lambda: self.shooter.run(self.shooter.spinUp)
			.until(
				lambda: (
					self.shooter.atSpeed()
					and self.shooter.state == ShooterState.SPINUP_PIGEON
				)
				or not self.shooter.allowSpinup
			)
			.execute()
		)

		# TODO: Remaining binds

	def getAutonomousCommand(self) -> commands2.Command:
		return commands2.InstantCommand()
