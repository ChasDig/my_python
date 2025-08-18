from patterns.structural.bridge import PlayStation, Computer, GamePad, KeyboardAndMouse


def test_bridge():
    play_station_with_gamepad = PlayStation(implementation=GamePad())
    computer_with_gamepad = Computer(implementation=GamePad())
    computer_with_keyboard_and_mouse = Computer(implementation=KeyboardAndMouse())

    assert play_station_with_gamepad.base_operation() == "console gaming on gamepad"
    assert computer_with_gamepad.base_operation() == "computer gaming on gamepad"
    assert computer_with_keyboard_and_mouse.base_operation() == "computer gaming on keyboard and mouse"
