import subprocess

class GPS():
    def __init__(self):
        self.time = 0.
        self.longitude = 0.
        self.latitude = 0.
        self.altitude = 0.
        self.satellites = 0.
        self.speeds = 0.
        self.direction = 0.
        self.DS18B20_temperature = [0., 0.]
        self.battery_voltage = 0.
        self.BMP180_temperature = 0.
        self.pressure = 0.
        self.maximum_altitude = 0.
        self.DS18B20_count = 0.

def run():
    # initialise variables
    # pin allocations
    NTX2B_enable = 0
    UBLOX_enable = 2

    SSDV_folder = "/home/pi/pits/tracker/images"


    if (get_prog_count() > 1)
	{
		print("The tracker program is already running!")
		print("It is started automatically, with the camera script, when the Pi boots.\n")
		print("If you just want the tracker software to run, it already is,")
		print("and its output can be viewed on a monitor attached to a Pi video socket.\n")
		print("If instead you want to view the tracker output via ssh,")
		print("then you should first stop it by typing the following command:")
		print("	sudo killall tracker\n")
		print("and then restart manually with")
		print("	sudo ./tracker\n")
	}

	print("\nRASPBERRY PI-IN-THE-SKY FLIGHT COMPUTER")
	print(    "=======================================\n")

    if (new_board() > 0):
        if (new_board() == 2):
            print("RPi 2 B")
        else:
            print("RPi Model A+ or B+")

        print("PITS+ Board\n")

        led_ok = 25;
        led_warn = 24;
        sda = 2;
        scl = 3;

        set_all_config(led_ok, led_warn, sda, scl)

    else:
        print("RPi Model A+ or B+")
        print("PITS+ Board\n")

        led_ok = 11;
        led_warn = 4;
        sda = 5;
        scl = 6;

        set_all_config(led_ok, led_warn, sda, scl)

    set_monitor()
    set_camera()

    gps = GPS()




if __name__ == "__main__":
    run()
