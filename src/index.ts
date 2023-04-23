import * as express from "express";
import Logger from "./utils/Logger.js";
import dotenv from "dotenv";
import { BaseRoute } from "./routes/scaffolding/BaseRoute.js";
import { RouteResolver } from "./utils/RouteResolver.js";
import util from 'util'
import { Database } from "./utils/Database.js";

// Load our environment variables
dotenv.config();

// Create our server
const server = express.default();

server.use(express.raw({ type: "*/*", limit: "2gb" }));

// Establish our middleware for the server
server.use("/", BaseRoute(null as any));
server.use("/", new RouteResolver("mappings.json").generate());

new Database(process.env.MONGO_URI || "").connect().then(() => {
    Logger.log("Connected to database.");
    server.listen(process.env.PORT || 3000);
})