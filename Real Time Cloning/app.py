import gradio as gr
import urllib
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from os import path
import random
from kivy.core.audio import SoundLoader 

from kivy.clock import Clock
story="Your Story"
type=["superhero","action","drama","horror","thriller","sci_fi"]
def StoryGeneration(text):
        TextToStory=  gr.Interface.load(name="spaces/BilalSardar/StoryGenerator")
        #story=TextToStory("sci_fi",text,"Generate Story",fn_index=0)
        story=TextToStory(100,text,fn_index=0)[0]
        return story
class VoiceOver(MDApp):
    
    def CloneVoice(self,args):
        Voice =  gr.Interface.load(name="spaces/BilalSardar/Voice-Cloning")
        try:
            # Error generating code
            Voice(self.input1.text,"record.wav",None,fn_index=0)
        except Exception as err:
            print(err)
            t=str(err)
            
        url = "https://bilalsardar-voice-cloning.hf.space/file="+t[38:len(t)-1]
        #url = "https://bilalsardar-voice-cloning.hf.space/file=Audio.wav"
        save_as = "file.mp3"
        
        data = urllib.request.urlopen(url)

        f = open(save_as,'wb')
        f.write(data.read())
        f.close()
        
        
    
    #flip 
    def flip(self):
        themes=['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.theme_cls.primary_palette="LightGreen"#themes[random.randint(0,17)]
        print("Theme Changed")
    #sound playing
    def playaudio(self,obj):
        sound = SoundLoader.load('file.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
    #Text Updating
    def textUpdate(self,obj):
        generatedStory=StoryGeneration(self.input.text)
        print(generatedStory)
        self.input1._update_text_options(story)
        
            
    def build(self):
        screen = MDScreen()
        #UI Widgets go here
        self.toolbar=MDToolbar(title="Bilal's VoiceOverTool")
        self.toolbar.pos_hint={"top":1}
        self.toolbar.right_action_items=[
        ["rotate-3d-variant",lambda x:self.flip()]]
        screen.add_widget(self.toolbar)
        
        
        #logo
        
        screen.add_widget(Image(
            source="Racconto.png",
            pos_hint={"center_x":0.5 ,"center_y":0.7}))
        
        #input
        
        self.input=MDTextField(
            text="Enter Prompt for Story",
            halign="center",
            size_hint=(0.8,1),
            pos_hint={"center_x":0.5 ,"center_y":0.4},
            font_size=22
        )
        
        self.input1=MDTextField(
            text="Your Story",
            halign="center",
            size_hint=(0.8,1),
            pos_hint={"center_x":0.5 ,"center_y":0.5},
            font_size=22
        )
        
        screen.add_widget(self.input)
        screen.add_widget(self.input1)
        
         #labels
        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.35},
            theme_text_color = "Secondary"
        )
        
        
        screen.add_widget(self.label)
     
       
        
        # "CONVERT" button
        screen.add_widget(MDFillRoundFlatButton(
            text="CLONE",
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y":0.15},
            on_press = self.CloneVoice
        ))
        screen.add_widget(MDFillRoundFlatButton(
            text="PLAY",
            font_size = 17,
            pos_hint = {"center_x": 0.3, "center_y":0.15},
            on_press = self.playaudio
        ))
        screen.add_widget(MDFillRoundFlatButton(
            text="STORY",
            font_size = 17,
            pos_hint = {"center_x": 0.7, "center_y":0.15},
            on_press = self.textUpdate
        ))
        
        return screen
    
    
if __name__ == '__main__':
    VoiceOver().run()
    
