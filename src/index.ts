import * as express from "express";
import Logger from "./utils/Logger.js";
import dotenv from "dotenv";
import { BaseRoute } from "./routes/scaffolding/BaseRoute.js";
import { RouteResolver } from "./utils/RouteResolver.js";
import util from 'util'
import cors from "cors";

// Load our environment variables
dotenv.config();

// Create our server
const server = express.default();

server.use(express.raw({ type: "*/*", limit: "2gb" }));
server.use(cors({
    allowedHeaders: "*"
}))

// Establish our middleware for the server
server.use("/", BaseRoute(null as any));
server.use("/", new RouteResolver("mappings.json").generate());