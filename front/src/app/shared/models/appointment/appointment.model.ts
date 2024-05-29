import { Beneficiary } from "../beneficiary";
import { Professional, Speciality } from "../professional";
import { Status } from "../swap";
import { Volunteer } from "../volunteer";

export class Appointment {
    constructor(
        public id?: number,
        public beneficiary?: Beneficiary,
        public professional?: Professional,
        public speciality?: Speciality,
        public volunteer?: Volunteer,
        public status?: Status,
        public datetime?: Date
    ) { }
}

export class AppointmentPOST {
    constructor(
        public id?: number,
        public beneficiary_id?: number,
        public professional_id?: number,
        public speciality_id?: number,
        public volunteer_id?: number,
        public status_id?: number,
        public datetime?: Date
    ) { }

    transformObjectToEdit(appointment: Appointment) {
        this.id = appointment.id;
        this.beneficiary_id = appointment.beneficiary?.id;
        this.professional_id = appointment.professional?.id;
        this.speciality_id = appointment.speciality?.id;
        this.volunteer_id = appointment.volunteer?.id;
        this.status_id = appointment.status?.id;
        this.datetime = appointment.datetime;
    }
}