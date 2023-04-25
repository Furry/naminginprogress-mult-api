import { Router } from "express";
import { Database } from "../../utils/Database.js";
import Logger from "../../utils/Logger.js";
import { Api } from "./Api.js";
import { Static } from "./Static.js";

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

    router.get("/", (_, res) => {
        // Send to discord server
        res.redirect("https://discord.gg/tamVs2Ujrf");
    })
    router.use("/api", Api(db));
    router.use("/s", Static());

    return router;
}