from dbElements import *

carrier_freq = BasicThing("CarFreq", "Carrier Frequency", 2e9, "Hz")

print(f"Current carrier frequency is: {carrier_freq.get(Unit='Hz')} Hz.")

print(f"\nSet carrier freq to 10 kHz.")
carrier_freq.set(10,"kHz")
print(f"Current carrier frequency is: {carrier_freq.get(Unit='Hz')} Hz.")

print(f"\nSet carrier freq to 100 'something'.")
carrier_freq.set(100)
print(f"Current carrier frequency is: {carrier_freq.get(Unit='Hz')} Hz.")

print(f"\nConvert to limited thing now, default limits")
carrier_freq_ltd = add_limits(carrier_freq)
carrier_freq_ltd.set(10,"kHz")
carrier_freq_ltd.set(10,"Hz")

print(f"\nConvert to limited thing now, set limits")
carrier_freq_ltd = add_limits(carrier_freq, 1.5e9, 3e9)
carrier_freq_ltd.set(10,"kHz")
carrier_freq_ltd.set(10,"Hz")


print(f"\n\n########### Creating Limited Thing now>")

carrier_freq = LimitedThing("CarFreqLtd", "Carrier Frequency Ltd", 2e9, "Hz", 1.5e9, 3e9)

print(f"Current carrier frequency is: {carrier_freq.get(Unit='Hz')} Hz.")

print(f"\nSet carrier freq to 10 kHz.")
carrier_freq.set(10,"kHz")
print(f"Current carrier frequency is: {carrier_freq.get(Unit='Hz')} Hz.")

print(f"\nSet carrier freq to 2.1 GHz.")
carrier_freq.set(2.1,"GHz")
print(f"Current carrier frequency is: {carrier_freq.get(Unit='Hz')} Hz.")

print(f"\nSet carrier freq to 100 'something'.")
carrier_freq.set(100)
print(f"Current carrier frequency is: {carrier_freq.get(Unit='Hz')} Hz.")

