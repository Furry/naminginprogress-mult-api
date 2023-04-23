import "colors";

export default class Logger {
    public static log(message: string, color: string = "white"): void {
        console.log(`[${new Date().toLocaleString()}]`.green, message[color as any]);
    }

    public static error(message: string, color: string = "red"): void {
        console.log(`[${new Date().toLocaleString()}]`.green, message[color as any]);
    }

    public static warn(message: string, color: string = "yellow"): void {
        console.log(`[${new Date().toLocaleString()}]`.green, message[color as any]);
    }
    
    public static series(init: string, ...components: any[]) {
        Logger.log(init + components.map(c => `\n\t| ${`${c}`.green}`))
    }
}