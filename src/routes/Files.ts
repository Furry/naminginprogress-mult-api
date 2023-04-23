import { raw, Router } from "express";
import { Database } from "../utils/Database.js";
import Logger from "../utils/Logger.js";
import path from "path";
import * as crypt from "../utils/Crypt.js";
import * as mime from "mime-types";
import * as fs from "fs";

export function Files(db: Database) {
    const router = Router();

    router.post("/upload", (req, res) => {
        const data =  Buffer.from(req.body);

        // Print all  headers
        const type: string | boolean = typeof req.headers["x-file-type"] === "string"
        // @ts-ignore
            ? req.headers["x-file-type"].replace(/image\//, "")
            : req.headers["x-file-name"]
            ? (req.headers["x-file-name"] as string).split(".").pop()!
            : mime.extension(req.headers["content-type"] as string);

        if (!type) {
            res.status(400).json({ error: "Invalid file type." });
            return;
        }

        const domains = (req.headers["domains"] as string || "http://naminginprogress.com").split(",");
        let domain = domains[Math.floor(Math.random() * domains.length)];

        // If it starts with http:// or https://, remove it.
        if (domain.startsWith("http://") || domain.startsWith("https://")) {
            domain = domain.substring(domain.indexOf("//") + 2);
        }

        const id = crypt.id(8);

        // If it's an image, save it without unnamed.
        const name = req.headers["x-file-name"] || "unnamed";
        let label = "";
        let newPath = "";
        if ([ "png", "jpg", "jpeg", "gif", "webp" ].includes(type) && name === "unnamed") {
            label = `${id}.${type}`;
            newPath = path.join(process.cwd(), `./static/uploads/${id}.${type}.bin`);
        } else {
            label = `${id}/${name}.${type}`;
            newPath = path.join(process.cwd(), `./static/uploads/${id}-${name}.${type}.bin`);
        }


        Logger.log("Writing file to" + newPath);
        fs.writeFileSync(newPath, data);

        res.json({
            at: Date.now(),
            url: `http://${domain}/s/${label}`
        })
    })

    return router;
}
