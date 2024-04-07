import serial
# import time

'''
Setup assumes we'll use GPIO 14 (pin 8) for Tx, GPIO15 (pin 10) for Rx
prep commands: 
sudo raspi-config. 
Go to interfacing Options > Serial. 
Select No for login shell to be accessible over serial. 
Select Yes for serial port hardware to be enabled.
'''
# Setup serial connection (Change this port if needed)
ser = serial.Serial('/dev/serial0', 9600, timeout=1)
ser.flush()

# parameter: result form stockFish. Parsed into a string.
def sendResultsToArduino(result):
    while True:
        ser.write(1)
    '''
    # code for reading input from Arduino. Uncomment if needed
    time.sleep(1)  # Wait for a second
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
    '''

sendResultsToArduino("HAI")