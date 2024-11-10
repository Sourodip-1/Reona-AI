from pynput.keyboard import Controller
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER


def volume_up():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get current volume level
    current_volume = volume.GetMasterVolumeLevelScalar()
    # print(f"Current Volume: {current_volume * 100:.2f}%")

    # Increase volume by a specific amount (e.g., 5%)
    increase_amount = 0.05
    new_volume = min(1.0, current_volume + increase_amount)  # Ensure max volume is 1.0
    volume.SetMasterVolumeLevelScalar(new_volume, None)

def volume_down():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get current volume level
    current_volume = volume.GetMasterVolumeLevelScalar()
    # print(f"Current Volume: {current_volume * 100:.2f}%")

    # Decrease volume by a specific amount (e.g., 5%)
    decrease_amount = 0.05
    new_volume = max(0.0, current_volume - decrease_amount)  # Ensure min volume is 0.0
    volume.SetMasterVolumeLevelScalar(new_volume, None)

