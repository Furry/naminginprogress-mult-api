import { Router } from "express";
import Logger from "../../utils/Logger.js";
import { Files } from "../Files.js";

export function Api() {
    const router = Router();

    router.use("/files", Files());

    return router;
}