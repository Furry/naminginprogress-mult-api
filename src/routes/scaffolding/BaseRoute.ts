import { Router } from "express";
import { Database } from "../../utils/Database.js";
import Logger from "../../utils/Logger.js";
import { Api } from "./Api.js";
import { Static } from "./Static.js";
import fs from "fs";
import path from "path";

export function BaseRoute(db: Database) {
    const router = Router();

    // Establish our base middleware for logging requests.
    router.use((req, _, next) => {
        let ip = req.headers["x-forwarded-for"] || req.socket.remoteAddress;

        if (process.env.ISDEV === "true") {
            Logger.series("Incoming Request", req.method, req.url, ip);
        }

        Database.Instance.col("requests").insertOne({
            at: Date.now(),
            ip,
            method: req.method,
            url: req.url
        })

        next();
    });
    
    router.use("/api", Api(db));
    router.use("/s", Static());
    router.get("*", (req, res) => {
        // Check if there's a matching file in the web directory. If so, serve it, else redirect to discord.
        if (req.url != "/") {
            let fname = req.url.split("/")[1];
            if (fs.existsSync(`./static/web/${fname}.html`)) {
                return res.sendFile(path.resolve(`./static/web/${fname}.html`));
            }
        }
        // Send to discord server
        res.redirect("https://discord.gg/tamVs2Ujrf");
    })

    return router;
}