from pynput.keyboard import Controller # type: ignore
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume # type: ignore
from comtypes import CLSCTX_ALL # type: ignore# type: ignore
from ctypes import cast, POINTER# type: ignore
from ctypes import cast, POINTER# type: ignore# type: ignore
from comtypes import CLSCTX_ALL# type: ignore
from win32com.client import GetObject# type: ignore
from win32com.client import Dispatch# type: ignore
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume# type: ignore

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

    # Decrease volume by a specific amount (e.g., 10%)
    decrease_amount = 0.10
    new_volume = max(0.0, current_volume - decrease_amount)  # Ensure min volume is 0.0
    volume.SetMasterVolumeLevelScalar(new_volume, None)

def volume_set():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get current volume level
    current_volume = volume.GetMasterVolumeLevelScalar()
    # print(f"Current Volume: {current_volume * 100:.2f}%")

    # Decrease volume by a specific amount (e.g., 10%)
    decrease_amount = 0.10
    new_volume = max(0.0, current_volume - decrease_amount)  # Ensure min volume is 0.0
    volume.SetMasterVolumeLevelScalar(new_volume, None)

