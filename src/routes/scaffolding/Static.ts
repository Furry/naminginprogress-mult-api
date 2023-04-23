import { Router } from "express";
import fs from "fs";

export function Static() {
    const router  = Router();

    router.get("/*", (req, res) => {
        console.log(req.url);
        let ref = req.url.substring(1);
        ref = ref.replaceAll("/", "-");
        ref = ref + ".bin";

        console.log("Looking for file", ref);

        if (fs.existsSync(`./static/uploads/${ref}`)) {
            const data = fs.readFileSync(`./static/uploads/${ref}`);
            const name = req.url.split("/").pop();

            // If the file is an image, set the content type to the image type.
            if (name?.endsWith(".png") || name?.endsWith(".jpg") || name?.endsWith(".jpeg")) {
                res.setHeader("Content-Disposition", "inline");
                res.setHeader("Content-Type", "image/png");
                console.log("Displaying inline");
            } else {
                res.setHeader("Content-Type", "binary/octet-stream")
                res.setHeader(
                    "Content-Disposition", 
                    `attachment; filename="${name}"`);
            }

            res.send(data);
        } else {
            res.status(404).send("Not Found");
        }
    })

    return router;
}
