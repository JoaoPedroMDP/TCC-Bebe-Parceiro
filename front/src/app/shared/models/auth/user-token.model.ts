export class UserToken {
    constructor(
    public expiry?: string,
    public token?: string,
    public user?: User
    ) { }
}

export class User {
    constructor(
        public id?: number,
        public username?: string,
        public name?: string,
        public email?: string,
        public phone?: string,
        public groups?: Group[]
    ) { }
}

export class Group {
    constructor(
        public id?: number,
        public name?: string,
        public permissions?: Permission[]
    ) { }
}

export class Permission {
    constructor(
        public id?: number,
        public name?: string
    ) { }
}



