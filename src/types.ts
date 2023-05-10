export type GenericObject = { [key: string] : any }

export interface Direct {
    [key: string]: {
        method: "GET" | "POST" | "PUT" | "DELETE" | "PATCH" | "OPTIONS" | "HEAD";
        alias: string
    }
}
export interface App {
    location: string;
    invoke: string;
    entry: string;
    args: string;
    port: number;
    directs: Direct;
}

export interface RouteMap {
    apps: App[]
}