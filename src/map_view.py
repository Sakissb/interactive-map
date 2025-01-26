from kivy.uix.widget import Widget
from kivy_garden.mapview import MapView as KivyMapView, MapMarkerPopup


class MapView(Widget):
    def __init__(self, **kwargs):
        super(MapView, self).__init__(**kwargs)
        self.map = KivyMapView(zoom=10, lat=0, lon=0)
        self.markers = []
        self.add_widget(self.map)
        self.setup_map()

    def setup_map(self):
        # Initialize the map rendering here
        self.render()

    def add_marker(self, location, title):
        # Add a marker to the map
        marker = MapMarkerPopup(lat=location[0], lon=location[1])
        self.map.add_marker(marker)
        self.markers.append({'location': location, 'title': title})
        self.update_map()

    def update_map(self):
        # Update the map with the current markers
        self.render()

    def on_user_interaction(self, event):
        # Handle user interactions with the map
        pass

    def render(self):
        # Render the map and markers
        print("Rendering map with markers:", self.markers)
