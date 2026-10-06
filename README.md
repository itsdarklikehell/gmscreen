# GM Screen

A multi-screen presentation tool, initially built for tabletop gaming sessions.

## Features

- **Multi-Screen Support**: Create and manage multiple view systems with individual viewports
- **Playlist Management**: Organize media into playlists for each view system
- **Play States**: Define combined states (background, music, video) for viewports
- **Dark Mode**: Toggle between light and dark themes with system preference detection
- **PWA Support**: Install as a Progressive Web App for offline access
- **Export/Import**: Backup and restore all data as JSON files
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Screenshots

![GM Screen Dashboard](screenshots/dashboard.png)
![GM Screen System](screenshots/system.png)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/itsdarklikehell/gmscreen.git
   cd gmscreen
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:
   ```bash
   python runserver.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

### Production Deployment

```bash
gunicorn -w 4 -b 0.0.0.0:5000 gmscreen:app
```

## Usage

### Creating a View System

1. Click "New System" in the navbar
2. Enter a name and optional location
3. Click "Save"

### Adding Viewports

1. Click on a system to view details
2. Add viewports with unique codes
3. Viewports can be accessed at `/viewport/<code>`

### Managing Playlists

1. Create playlists for each system
2. Add play states to define media combinations
3. Play states can be activated on viewports

### Exporting/Importing Data

1. Click "Export" to download all data as JSON
2. Click "Import" to restore from a backup file
3. Data includes systems, viewports, playlists, and play states

### Dark Mode

- Click the moon/sun icon in the top-right corner to toggle dark mode
- The app respects your system preference by default
- Your preference is saved in localStorage

## PWA Installation

1. Open GM Screen in Chrome or Edge
2. Click the install icon in the address bar
3. Follow the prompts to install
4. Launch from your home screen or app drawer

## API Endpoints

### Systems
- `GET /api/systems` - List all systems
- `POST /api/systems` - Create a new system
- `GET /api/systems/<id>` - Get a specific system
- `PUT /api/systems/<id>` - Update a system
- `DELETE /api/systems/<id>` - Delete a system

### Viewports
- `GET /api/viewports` - List all viewports
- `POST /api/viewports` - Create a new viewport
- `GET /api/viewports/<id>` - Get a specific viewport
- `PUT /api/viewports/<id>` - Update a viewport
- `DELETE /api/viewports/<id>` - Delete a viewport

### Playlists
- `GET /api/playlists` - List all playlists
- `POST /api/playlists` - Create a new playlist
- `GET /api/playlists/<id>` - Get a specific playlist
- `PUT /api/playlists/<id>` - Update a playlist
- `DELETE /api/playlists/<id>` - Delete a playlist

### Play States
- `GET /api/playstates` - List all play states
- `POST /api/playstates` - Create a new play state
- `GET /api/playstates/<id>` - Get a specific play state
- `PUT /api/playstates/<id>` - Update a play state
- `DELETE /api/playstates/<id>` - Delete a play state

### Export/Import
- `GET /api/export` - Export all data as JSON
- `POST /api/import` - Import data from JSON

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

See [LICENSE](LICENSE) for more information.
