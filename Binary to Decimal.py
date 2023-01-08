from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton, MDFlatButton

class main(MDApp):
    def clear(self, args):
        self.text_input.text = ''
    def convert(self, args):
        a = int(self.text_input.text, 2)
        self.converted.text = str(a)
        self.label.text = 'In Decimal'

    def build(self):
        s = MDScreen()
        # Adding toolbar for the title
        self.toolbar = MDTopAppBar(
            title='Binary to decimal', pos_hint={'top': 1}
        )
        #self.toolbar.right_action_items = [['rotate-3d-variant', lambda x: self.flip()]]
        # adding text input
        self.text_input = MDTextField(hint_text='Enter the binary number',
                                      pos_hint={'center_x': 0.5, 'center_y': 0.6},
                                      halign='center', size_hint=(0.8, 1))
        # adding label secondary
        self.label = MDLabel(halign='center',
                             pos_hint={'center_x': 0.50, 'center_y': 0.4},
                             theme_text_color='Secondary')
        # adding label primary
        self.converted = MDLabel(halign='center',
                                 pos_hint={'center_x': 0.5, 'center_y': 0.31},
                                 theme_text_color='Primary', font_style='H5')
        # adding the converter button
        self.button = MDFillRoundFlatButton(text='CLICK TO CONVERT',
                                            pos_hint={'center_x': 0.5, 'center_y': 0.2},
                                            halign='center', theme_text_color='Primary',
                                            font_style='H6', on_press=self.convert)
        self.dismiss = MDFlatButton(text='CLEAR',
                                    pos_hint={'center_x': 0.5, 'center_y': 0.1},
                                    halign='center', theme_text_color='Primary',
                                    font_style='H6', on_press=self.clear)
        s.add_widget(self.dismiss)
        s.add_widget(self.button)
        s.add_widget(self.converted)
        s.add_widget(self.label)
        s.add_widget(self.text_input)
        s.add_widget(self.toolbar)
        return s