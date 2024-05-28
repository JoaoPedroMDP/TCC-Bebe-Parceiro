import { Beneficiary } from "../beneficiary"
import { Professional, Speciality } from "../professional"
import { Status } from "../swap"
import { Volunteer } from "../volunteer"

export class Appointment {
    constructor(
        public id?: number,
        public beneficiary?: Beneficiary,
        public professional?: Professional,
        public speciality?: Speciality,
        public volunteer?: Volunteer,
        public status?: Status,
        public datetime: Date = new Date()
    ) { }
}

