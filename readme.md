# NamingInProgress API
It's basically just a TypeScript server that has the ability to spawn additional servers and manage them, acting as a middleman and embarassing reverse proxy for integration of python ML models.

## Installation
``$ yarn / npm install``
## Usage
``$ yarn start / npm start``

## API
GET /api/stats
 - Returns the current stats of the api, information about common requests and their counts.

GET /upload
 - Returns the upload page, which is a simple form that allows you to upload a file / image to the server.

GET /dash
 - Returns the dashboard page, a simple streamlit render showing some of the rendered statistics.

POST /api/upload
    - Uploads a file to the server, and returns the path as a url to the file
    - The files are given a unique ID and renamed to avoid collisions and risk to the server.
    - See src/routes/Files.ts for usage

POST /ai/vulgarity
    - Returns the vulgarity of the text passed in the body.
    - Disabled in production because I can't afford a server that has more than 1gb of ram for the model :(

GET /s/*
    - Access one of the files uploaded to the server by url, this handles renaming it and normalizing extensions before it's served.

GET /*
    - Routes to my discord server for support or publicity
