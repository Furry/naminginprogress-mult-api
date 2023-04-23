import * as crypto from "crypto";

export function id(len: number): string {
    const hexstring = crypto.randomBytes(Math.ceil(len / 2)).toString("hex");
    return hexstring.slice(0, len);
}