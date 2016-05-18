# SimpleHTTPServer_Setup

This project allows to serve Mapbox Vector Tiles from localhost and visualize them using Leaflet Mapbox Vector Tiles.
If you have an mbtiles sqlite database of mapbox vector tiles, that is, protobuf encoded tiles according to 
[vector-tile-spec](https://www.mapbox.com/developers/vector-tiles/) and you want to easily visualize the tiles that are in there you can proceed as follows:

1. Extract the tiles to a directory structure with [mbutil](https://github.com/mapbox/mbutil.git)

    `mb-ubil someplace.mbtiles --image_format=pbf tiles `
  
    This will output all your mvts to the tiles directory with the z/x/y.pbf hierarchy

2. From the `tiles` folder run:

    `python simple_http_server.py <port-number>`


