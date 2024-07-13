from pint import UnitRegistry
from math import pi, tau

driverControllerPort: int = 0
operatorControllerPort: int = 1

unit: UnitRegistry = UnitRegistry()

class Drive:
	# MODULES
	frontLeft: dict[int | float] = {  # noqa: RUF012
		"driveMotorId": 5,
		"turningMotorId": 6,
		"turningEncoderId": 11,
		"offset":-0.439 * unit.radian,
	}
	frontRight: dict[int | float] = {  # noqa: RUF012
		"driveMotorId": 1,
		"turningMotorId": 2,
		"turningEncoderId": 9,
		"offset":-1.592 * unit.radian,
	}
	rearLeft: dict[int | float] = {  # noqa: RUF012
		"driveMotorId": 7,
		"turningMotorId": 8,
		"turningEncoderId": 12,
		"offset":-2.180 * unit.radian,
	}
	rearRight: dict[int | float] = {  # noqa: RUF012
		"driveMotorId": 3,
		"turningMotorId": 4,
		"turningEncoderId": 10,
		"offset":3.073 * unit.radian,
	}

	wheelRadius = 2.0 * unit.inch
	wheelCircumference = wheelRadius * 2 * pi / unit.turn
	encoderResolution = 4096 #counts per rotation
	moduleMaxAngularVelocity = pi * unit.radian / unit.second
	moduleMaxAngularAcceleration = tau * unit.radian / unit.second / unit.second

	turnRatio = (150 / 7)
	driveRatio = (50 / 14) * (17 / 27) * (45 / 15)

	drive_p = .01
	drive_i = 0
	drive_d = 0
	drive_v = 12 / (100 / driveRatio)

	turn_p = 40
	turn_i = 0
	turn_d = 0

	# DRIVETRAIN
	maxSpeed = 3 * unit.meter / unit.second  # 3 meters per second
	maxAngularSpeed = pi * unit.radian / unit.second  # 1/2 rotation per second
	chassisLength = 31.5 * unit.inch

	gyroId = 20