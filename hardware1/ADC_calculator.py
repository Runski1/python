ref_voltage = float(input("Reference voltage: "))
resolution = int(input("Bit resolution: "))
mode = int(input("value to volts (0) / volts to value (1)"))
steps = (2 ** resolution) - 1
increment = ref_voltage / steps
variance = increment / 2

if mode == 0:
    num = int(input("Enter value: "))
    voltage = increment * num
    print("Voltage: " + str(voltage) + " +- " + str(variance))

elif mode == 1:
    voltage = float(input("Enter Volts: "))
    num = round(voltage / increment)
    print("Value: " + str(num))
