import * as MongoDB from "mongodb";

export class Database {
    private static _instance: Database = null as any;
    public static get Instance(): Database {
        return this._instance;
    }

    private _client: MongoDB.MongoClient = null as any;
    constructor(uri: string) {
        this._client = new MongoDB.MongoClient(uri);
        Database._instance = this;
    }

    public async connect(): Promise<void> {
        await this.client.connect();
    }

    public get client() {
        return this._client;
    }

    public get db() {
        return this._client.db("upload-extended");
    }

    public col(name: string) {
        return this.db.collection(name);
    }
}