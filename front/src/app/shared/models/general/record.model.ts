import { Beneficiary } from "../beneficiary";
import { Volunteer } from "../volunteer";
import { Evaluation } from "../general";

export class Record {
    id?: number;
    createdAt?: Date;
    updatedAt?: Date;
    description?: string;
    evaluation?: Evaluation;
    beneficiary?: Beneficiary;
    volunteer?: Volunteer;

    constructor(
        id: number,
        createdAt: Date,
        updatedAt: Date,
        description: string,
        evaluation: Evaluation,
        beneficiary: Beneficiary,
        volunteer: Volunteer
    ) {
        this.id = id;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
        this.description = description;
        this.evaluation = evaluation;
        this.beneficiary = beneficiary;
        this.volunteer = volunteer;
    }
}