# Interactive Map App

This project is an interactive map application focused on Greece, built using Python. It allows users to explore various locations, view map markers, and interact with the map interface.

## Project Structure

```
interactive-map-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── map_view.py      # Handles map rendering and user interactions
│   └── utils
│       └── __init__.py  # Utility functions and constants
├── requirements.txt      # Python dependencies
├── buildozer.spec        # Configuration for building the Android app
└── README.md             # Project documentation
```

## Features

- Interactive map of Greece
- User-friendly interface for exploring locations
- Map markers for various points of interest
- Responsive design for mobile devices

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/interactive-map-app.git
   cd interactive-map-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Build the application for Android using Buildozer:
   ```
   buildozer -v android debug
   ```

4. Deploy the app to your Android device:
   ```
   buildozer android deploy run
   ```

## Usage Guidelines

- Launch the app on your Android device.
- Explore the interactive map by tapping on different markers.
- Use pinch-to-zoom and swipe gestures to navigate the map.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.