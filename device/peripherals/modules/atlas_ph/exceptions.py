from device.peripherals.classes.atlas.exceptions import DriverError


class ReadPHError(DriverError):  # type: ignore
    message_base = "Unable to read pH"
