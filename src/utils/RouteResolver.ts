import { Router } from "express";
import fs from "fs";
import { RouteMap } from "../types.js";
import Logger from "./Logger.js";
import path from "path"
import childprocess from "child_process"

import * as Express from "express";

export class RouteResolver {
    private config: string;
    private routes: RouteMap;

    constructor(config: string) {
        this.config = config;
        this.routes = null as any;
    }

    private pathOfService(lang: string): string {
        return path.join(
            path.dirname(require.main?.filename || "./"),
            "../src/services",
            lang
        )
    }

    public generate(): Router {
        const router = Router();

        router.use(Express.raw({ type: "*/*", limit: "10kb" }))
        this.routes = JSON.parse(fs.readFileSync(this.config, "utf-8"));

        for (const appName in this.routes["apps"]) {
            const app = this.routes["apps"][appName];
            Logger.series(`Binding ${appName}`);

            const entry = path.join(
                this.pathOfService(app.location),
                app.entry
            )

            // Start the application using app.invoke
            childprocess.spawn(app.invoke, [entry], {
                env: {
                    ...process.env,
                    PORT: app.port.toString()
                }
            });

            // Bind the direct routes.
            for (const directName in app.directs) {
                // @ts-ignore
                router[app.directs[directName].method.toLowerCase()]("/api" + directName, (req: Express.Request, res: Express.Response) => {
                    // Resend the request to localhost as if it were a proxy
                    fetch(`http://127.0.0.1:${app.port}/${app.directs[directName].alias}`, {
                        method: req.method,
                        body: req.body
                    }).then(async (response) => {
                        for (const header of response.headers.keys()) {
                            res.setHeader(header, response.headers.get(header)!);
                        }
                        res.status(response.status).send(await response.text());
                    })
                })
            }
        }

        return router;
    }
}