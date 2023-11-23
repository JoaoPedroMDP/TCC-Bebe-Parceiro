import { Country } from "./index"

export class State {
    constructor(
        public id?: number,
        public name?: string,
        public country?: Country
    ) { }
}
