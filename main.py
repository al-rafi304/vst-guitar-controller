from inputs import devices, get_gamepad
import keyboard
import datetime
import sys

# Get the list of available input devices
gamepads = devices.gamepads

if gamepads == None:
    print("No Gamepad Detected !")
else:

    print("----------Script Started----------")
    startTime = datetime.datetime.now()

    allowStroke = True
    allowSwitch = True

    chordBtnList = [
        ['z', 'b', 'n', 'v', 'm'],
        ['s', 'x', 'd', 'c', 'g']
    ]

    chordListIndex = 0

    # Event loop to continuously read gamepad inputs
    while True:
        events = get_gamepad()
        for event in events:

            # Downstroke
            if event.code == 'ABS_Y' and event.state < 0 and allowStroke== True:
                keyboard.press(",")
                allowStroke = False
                print('▼ Downstroke')

            # Upstroke
            if event.code == 'ABS_Y' and event.state > 0 and allowStroke== True:
                keyboard.press("2")
                allowStroke = False
                print('▲ Upstroke')

            # Switch Chord List
            if event.code == 'ABS_RY' and event.state < 0 and allowSwitch== True:
                chordListIndex = (chordListIndex + 1) % len(chordBtnList)
                allowSwitch = False
                print('⇋ SWTICHED CHORD LIST ⇋')

            # Mute
            if event.code == 'BTN_TL' and event.state == 1:
                keyboard.press("3")
                print('|| Mute')


            # Chord 1
            if event.code == "BTN_EAST" and event.state == 1:
                keyboard.press_and_release(chordBtnList[chordListIndex][0])
                print(': Chord 1')
            # Chord 2
            if event.code == "BTN_SOUTH" and event.state == 1:
                keyboard.press_and_release(chordBtnList[chordListIndex][1])
                print(': Chord 2')
            # Chord 3
            if event.code == "BTN_WEST" and event.state == 1:
                keyboard.press_and_release(chordBtnList[chordListIndex][2])
                print(': Chord 3')
            # Chord 4
            if event.code == "BTN_NORTH" and event.state == 1:
                keyboard.press_and_release(chordBtnList[chordListIndex][3])
                print(': Chord 4')
            # Chord 4
            if event.code == "BTN_SELECT" and event.state == 1:
                keyboard.press_and_release(chordBtnList[chordListIndex][4])
                print(': Chord 5')

            # 6th String
            if event.code == 'ABS_HAT0Y' and event.state == -1:
                keyboard.press_and_release('w')
                print('҂ 6th String')
            # 1st String
            if event.code == 'ABS_HAT0Y' and event.state == 1:
                keyboard.press_and_release('u')
                print('҂ 1st String')
            # 4th String
            if event.code == 'ABS_HAT0X' and event.state == -1:
                keyboard.press_and_release('r')
                print('҂ 4th String')
            # 3rd String
            if event.code == 'ABS_HAT0X' and event.state == 1:
                keyboard.press_and_release('t')
                print('҂ 3rd String')
            

            # Button releases
            if event.code == 'ABS_Y' and event.state == 0:
                keyboard.release(",")
                keyboard.release("2")
                allowStroke = True
            if event.code == 'BTN_TL' and event.state == 0:
                keyboard.release('3')
            if event.code == 'ABS_RY' and event.state == 0:
                allowSwitch = True


            if event.code == 'BTN_START' and event.state == 1:
                endTime = datetime.datetime.now()
                totalTime = endTime - startTime
                sys.exit(f"\n----------Script Terminated---------- \nTotal time passed: {round(totalTime.seconds / 60, 2)}m")
            
            # print(event.code, event.state, end='\n\n')