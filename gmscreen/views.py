from flask import request, jsonify, render_template, send_from_directory
from gmscreen import app
from gmscreen.database import db, ViewSystem, Viewport, Playlist, PlayState
import json
import os


@app.route('/')
def index():
    """Render the main dashboard."""
    return render_template('index.html')


@app.route('/api/systems', methods=['GET'])
def get_systems():
    """Get all view systems."""
    systems = ViewSystem.query.all()
    return jsonify([s.to_dict() for s in systems])


@app.route('/api/systems', methods=['POST'])
def create_system():
    """Create a new view system."""
    data = request.get_json()
    system = ViewSystem(
        name=data.get('name'),
        location=data.get('location')
    )
    db.session.add(system)
    db.session.commit()
    return jsonify(system.to_dict()), 201


@app.route('/api/systems/<int:system_id>', methods=['GET'])
def get_system(system_id):
    """Get a specific view system."""
    system = ViewSystem.query.get_or_404(system_id)
    return jsonify(system.to_dict())


@app.route('/api/systems/<int:system_id>', methods=['PUT'])
def update_system(system_id):
    """Update a view system."""
    system = ViewSystem.query.get_or_404(system_id)
    data = request.get_json()
    system.name = data.get('name', system.name)
    system.location = data.get('location', system.location)
    db.session.commit()
    return jsonify(system.to_dict())


@app.route('/api/systems/<int:system_id>', methods=['DELETE'])
def delete_system(system_id):
    """Delete a view system."""
    system = ViewSystem.query.get_or_404(system_id)
    db.session.delete(system)
    db.session.commit()
    return '', 204


@app.route('/api/viewports', methods=['GET'])
def get_viewports():
    """Get all viewports."""
    viewports = Viewport.query.all()
    return jsonify([v.to_dict() for v in viewports])


@app.route('/api/viewports', methods=['POST'])
def create_viewport():
    """Create a new viewport."""
    data = request.get_json()
    viewport = Viewport(
        viewsystem_id=data.get('viewsystem_id'),
        name=data.get('name'),
        code=data.get('code')
    )
    db.session.add(viewport)
    db.session.commit()
    return jsonify(viewport.to_dict()), 201


@app.route('/api/viewports/<int:viewport_id>', methods=['GET'])
def get_viewport(viewport_id):
    """Get a specific viewport."""
    viewport = Viewport.query.get_or_404(viewport_id)
    return jsonify(viewport.to_dict())


@app.route('/api/viewports/<int:viewport_id>', methods=['PUT'])
def update_viewport(viewport_id):
    """Update a viewport."""
    viewport = Viewport.query.get_or_404(viewport_id)
    data = request.get_json()
    viewport.name = data.get('name', viewport.name)
    viewport.code = data.get('code', viewport.code)
    db.session.commit()
    return jsonify(viewport.to_dict())


@app.route('/api/viewports/<int:viewport_id>', methods=['DELETE'])
def delete_viewport(viewport_id):
    """Delete a viewport."""
    viewport = Viewport.query.get_or_404(viewport_id)
    db.session.delete(viewport)
    db.session.commit()
    return '', 204


@app.route('/api/playlists', methods=['GET'])
def get_playlists():
    """Get all playlists."""
    playlists = Playlist.query.all()
    return jsonify([p.to_dict() for p in playlists])


@app.route('/api/playlists', methods=['POST'])
def create_playlist():
    """Create a new playlist."""
    data = request.get_json()
    playlist = Playlist(
        viewsystem_id=data.get('viewsystem_id'),
        name=data.get('name')
    )
    db.session.add(playlist)
    db.session.commit()
    return jsonify(playlist.to_dict()), 201


@app.route('/api/playlists/<int:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    """Get a specific playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)
    return jsonify(playlist.to_dict())


@app.route('/api/playlists/<int:playlist_id>', methods=['PUT'])
def update_playlist(playlist_id):
    """Update a playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)
    data = request.get_json()
    playlist.name = data.get('name', playlist.name)
    db.session.commit()
    return jsonify(playlist.to_dict())


@app.route('/api/playlists/<int:playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    """Delete a playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)
    db.session.delete(playlist)
    db.session.commit()
    return '', 204


@app.route('/api/playstates', methods=['GET'])
def get_playstates():
    """Get all play states."""
    states = PlayState.query.all()
    return jsonify([s.to_dict() for s in states])


@app.route('/api/playstates', methods=['POST'])
def create_playstate():
    """Create a new play state."""
    data = request.get_json()
    state = PlayState(
        name=data.get('name'),
        background_uri=data.get('background_uri'),
        music_uri=data.get('music_uri'),
        video_uri=data.get('video_uri')
    )
    db.session.add(state)
    db.session.commit()
    return jsonify(state.to_dict()), 201


@app.route('/api/playstates/<int:state_id>', methods=['GET'])
def get_playstate(state_id):
    """Get a specific play state."""
    state = PlayState.query.get_or_404(state_id)
    return jsonify(state.to_dict())


@app.route('/api/playstates/<int:state_id>', methods=['PUT'])
def update_playstate(state_id):
    """Update a play state."""
    state = PlayState.query.get_or_404(state_id)
    data = request.get_json()
    state.name = data.get('name', state.name)
    state.background_uri = data.get('background_uri', state.background_uri)
    state.music_uri = data.get('music_uri', state.music_uri)
    state.video_uri = data.get('video_uri', state.video_uri)
    db.session.commit()
    return jsonify(state.to_dict())


@app.route('/api/playstates/<int:state_id>', methods=['DELETE'])
def delete_playstate(state_id):
    """Delete a play state."""
    state = PlayState.query.get_or_404(state_id)
    db.session.delete(state)
    db.session.commit()
    return '', 204


@app.route('/api/export', methods=['GET'])
def export_data():
    """Export all data as JSON."""
    data = {
        'version': '1.0',
        'systems': [s.to_dict() for s in ViewSystem.query.all()],
        'viewports': [v.to_dict() for v in Viewport.query.all()],
        'playlists': [p.to_dict() for p in Playlist.query.all()],
        'playstates': [s.to_dict() for s in PlayState.query.all()]
    }
    return jsonify(data)


@app.route('/api/import', methods=['POST'])
def import_data():
    """Import data from JSON."""
    data = request.get_json()
    
    PlayState.query.delete()
    Playlist.query.delete()
    Viewport.query.delete()
    ViewSystem.query.delete()
    db.session.commit()
    
    for system_data in data.get('systems', []):
        system = ViewSystem(
            name=system_data.get('name'),
            location=system_data.get('location')
        )
        db.session.add(system)
    db.session.commit()
    
    for viewport_data in data.get('viewports', []):
        viewport = Viewport(
            viewsystem_id=viewport_data.get('viewsystem_id'),
            name=viewport_data.get('name'),
            code=viewport_data.get('code')
        )
        db.session.add(viewport)
    db.session.commit()
    
    for playlist_data in data.get('playlists', []):
        playlist = Playlist(
            viewsystem_id=playlist_data.get('viewsystem_id'),
            name=playlist_data.get('name')
        )
        db.session.add(playlist)
    db.session.commit()
    
    for state_data in data.get('playstates', []):
        state = PlayState(
            name=state_data.get('name'),
            background_uri=state_data.get('background_uri'),
            music_uri=state_data.get('music_uri'),
            video_uri=state_data.get('video_uri')
        )
        db.session.add(state)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Import completed successfully'})


@app.route('/sw.js')
def service_worker():
    """Serve service worker."""
    return send_from_directory('static', 'sw.js')


@app.route('/manifest.json')
def manifest():
    """Serve PWA manifest."""
    return send_from_directory('static', 'manifest.json')


@app.route('/static/<path:path>')
def static_files(path):
    """Serve static files."""
    return send_from_directory('static', path)
