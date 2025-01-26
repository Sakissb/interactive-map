from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from map_view import MapView


class MainApp(App):
    def build(self):
        layout = BoxLayout()
        map_view = MapView()
        layout.add_widget(map_view)
        return layout


if __name__ == '__main__':
    MainApp().run()
