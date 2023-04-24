import { Router } from "express";
import { Database } from "../../utils/Database.js";
import Logger from "../../utils/Logger.js";
import { Files } from "../Files.js";

export function Api(db: Database) {
    const router = Router();

    router.use("/files", Files(db));

    router.get("/stats", async (req, res) => {
        // Find all requests in the last 24 hours, 7 days, and 30 days.
        const requests = await Database.Instance.col("requests").find({
            at: {
                $gt: Date.now() - 1000 * 60 * 60 * 24 * 30
            }
        }).toArray();

        requests.map(r => {
            // @ts-ignore
            delete r._id;
            delete r.ip;

            if (r.url.startsWith("/s/")) {
                r.url = "/s/"
            }

            return r;
        })

        const last1h = requests.filter(r => r.at > Date.now() - 1000 * 60 * 60).length;
        const last24h = requests.filter(r => r.at > Date.now() - 1000 * 60 * 60 * 24).length;
        const last7d = requests.filter(r => r.at > Date.now() - 1000 * 60 * 60 * 24 * 7).length;
        const last30d = requests.filter(r => r.at > Date.now() - 1000 * 60 * 60 * 24 * 30).length;

        // Get number of posts for each day in the last 30 days.
        const posts = await Database.Instance.col("posts").find({
            at: {
                $gt: Date.now() - 1000 * 60 * 60 * 24 * 30
            }
        }).toArray();

        const postsByDay = requests.map(p => {
            const date = new Date(p.at);
            return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
        }).reduce((acc, cur) => {
            if (acc[cur]) {
                acc[cur]++;
            } else {
                acc[cur] = 1;
            }
            return acc;
        }, {} as { [key: string]: number });

        // Fill in all days with 0 posts.
        for (let i = 0; i < 30; i++) {
            const date = new Date(Date.now() - 1000 * 60 * 60 * 24 * i);
            const key = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
            if (!postsByDay[key]) {
                postsByDay[key] = 0;
            }
        }

        // Sort the most used endpoints by number of requests.
        let endpoints = requests.map(r => r.url).reduce((acc, cur) => {
            if (acc[cur]) {
                acc[cur]++;
            } else {
                acc[cur] = 1;
            }
            return acc;
        }, {} as { [key: string]: number })

        // Sort endpoints 
        endpoints = Object.keys(endpoints).sort((a, b) => endpoints[b] - endpoints[a]).map(e => {
            return {
                url: e,
                requests: endpoints[e]
            }
        });

        endpoints = endpoints.slice(0, 10);

        res.json({
                last1h,
                last24h,
                last7d,
                last30d,
                postsByDay,
                endpoints: endpoints
            })
        })

    return router;
}