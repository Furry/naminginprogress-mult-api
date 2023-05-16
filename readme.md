<div style="text-align: center">
<table align="center">
  <tr>
    <td><img src="https://cdn.cdnlogo.com/logos/t/96/typescript.svg" alt="logo" width="50" height="50"></td>
    <td><h1>Naming In Progress API</h1></td>
  </tr>
</table>

<br>
<!-- Badges -->
<img src="https://img.shields.io/github/commit-activity/m/furry/naminginprogress-mult-api?style=for-the-badge" />
<img src="https://img.shields.io/discord/769020183540400128?style=for-the-badge" />
</div>

# Features
 - 🧩 Modular
 - ↩️ Reverse HTTP Routing
 - ⚡️ Fast with Express
 - 🔒 Middleware guarded endpoints
 - 📈 Statistics
 - 📓 Fluid TS typings

# Installation
To setup the application, you can use your favorite package TS package manager (NPM or Yarn), and clone the repository.

``$ yarn / npm install`` to install the dependencies

``$ yarn go / npm run go`` to start the application

# Configuration
The application is configured using a .env file, which is loaded using the dotenv package. The .env file is not included in the repository, so you will need to create one yourself.

``$ touch .env`` to create the file

``$ nano .env`` to edit the file

``$ cat .env`` to view the file

**.env parameteres:**
 - ISDEV: bool -- Whether or not the application is in development mode, this enables some features such as the dashboard and statistics. Is optional.
 - MONGO_URI: string -- The URI to the MongoDB database, this is used for the statistics and the file upload system. Is required.
 - PORT: number -- The port to run the server on, defaults to 8080 and is optional.
# Usage
``$ yarn start / npm start``

## API

**GET /api/stats**
- Returns the current stats of the API, information about common requests and their counts.

**GET /upload**
- Returns the upload page, which is a simple form that allows you to upload a file / image to the server.

**GET /dash**
- Returns the dashboard page, a simple Streamlit render showing some of the rendered statistics.

**POST /api/upload**
- Uploads a file to the server, and returns the path as a URL to the file.
- The files are given a unique ID and renamed to avoid collisions and risk to the server.
- See `src/routes/Files.ts` for usage.

**POST /ai/vulgarity**
- Returns the vulgarity of the text passed in the body.
- Disabled in production because I can't afford a server that has more than 1GB of RAM for the model :(

**GET /s/*** 
- Access one of the files uploaded to the server by URL, this handles renaming it and normalizing extensions before it's served.

**GET /*** 
- Routes to my Discord server for support or publicity.

# License / Commit Guidelines
This project is licensed under the MIT license, as for PRs or commits, go ahead!