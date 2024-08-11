from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.core.window import Window

class VideoPlayerApp(App):
    def build(self):
        # Create a vertical layout
        layout = BoxLayout(orientation='vertical')
        
        # Create a file chooser widget and set the initial path to 'C:\\'
        filechooser = FileChooserListView(path='C:\\')
        
        # Create a video player widget and allow it to stretch the video to fill its size
        video = VideoPlayer(options={'allow_stretch': True})
        
        # Create a button for toggling full screen
        #btn_fullscreen = Button(text='Toggle Fullscreen')
        
        # Add the file chooser, video player, and button to the layout
        layout.add_widget(filechooser)
        layout.add_widget(video)
        #layout.add_widget(btn_fullscreen)
        
        # Define a function that will be called when the selection of the file chooser changes
        def on_selection(*args):
            # Check if a file is selected
            if filechooser.selection:
                # Set the source of the video player to the selected file
                video.source = filechooser.selection[0]
                # Start playing the video
                video.state = 'play'
            else:
                print("No file selected.")
        
        # Bind the on_selection function to the selection event of the file chooser
        filechooser.bind(selection=on_selection)
        
        # Define a function that will be called when the button is pressed
        
        #def on_press(*args):
         #   video.fullscreen = not video.fullscreen
        
        # Bind the on_press function to the press event of the button
        #btn_fullscreen.bind(on_press=on_press)

        # Define different functions that will be called when 'Tab' key or 'P' key or 'M' key or 'F' key is pressed
        def on_key_down(window, key, *args):
            if key == 102:  # 102 is the keycode for 'F'
                video.fullscreen = not video.fullscreen

            if key == 9:  # 9 is the keycode for 'Tab'
                video.fullscreen = False

            elif key == 112:  # 112 is the keycode for 'P'

                if video.state == 'play':
                    video.state = 'pause'
                else:
                    video.state = 'play'

            elif key == 109:  # 109 is the keycode for 'M'

                if video.volume > 0:
                    video.volume = 0
                else:
                    video.volume = 1
            elif key == 115:  # 115 is the keycode for 'S'
                video.state = 'stop'        

        # Bind the on_key_down function to 'on_key_down' event of Window
        Window.bind(on_key_down=on_key_down)
        
        return layout

if __name__ == '__main__':
    # Create an instance of VideoPlayerApp and start it
    VideoPlayerApp().run()