# Video-Player-using-Python-Kivy
This is a simple local video player application built using the Kivy framework for Python. It allows the user to select a video file from their local file system and play it in the application. The application also includes functionality for toggling full screen mode, as well as keyboard shortcuts for controlling video playback.

## Requirements

### Python 3.x
### Kivy 2.0.0 or higher

## Installation

```bash
pip install kivy
```

## Usage

1) Use the file chooser widget to select a video file.
2) The video will begin playing automatically once a file is selected.
3) Press the 'Tab' key to exit full screen mode.
4) Press the 'F' key to toggle full screen mode.
5) Press the 'P' key to pause or play the video.
6) Press the 'M' key to mute or unmute the video.
7) Press the 'S' key to stop the video.

## Building the UI
The user interface for this application is built using Kivy's BoxLayout and VideoPlayer widgets. The BoxLayout widget is used to create a vertical layout, which contains a file chooser widget and a video player widget.

The file chooser widget is initialized with the initial path set to the root directory of the user's file system ('C:\' on Windows). The video player widget is initialized with the 'allow_stretch' option set to 'True', which allows the video to stretch to fill the widget's size.

## Event Handling
The application includes several event handlers for handling user input and controlling video playback.
1) The 'on_selection' event handler is called when the user selects a file in the file chooser widget. It sets the source of the video player widget to the selected file and begins playing the video.
2) The 'on_press' event handler (currently commented out) would be called when the user presses the full screen button. It would toggle the full screen mode of the video player widget.
3) The 'on_key_down' event handler is called when the user presses a key on the keyboard. It checks the keycode of the pressed key and performs an action accordingly.

## Conclusion
This application demonstrates how to build a simple local video player using the Kivy framework for Python. It includes functionality for selecting a video file, playing the video, and controlling video playback using keyboard shortcuts.

##Further Reading
1) Kivy Documentation
2) Kivy VideoPlayer Widget Documentation
3) Kivy FileChooser Widget Documentation
4) Kivy Keyboard Events Documentation
