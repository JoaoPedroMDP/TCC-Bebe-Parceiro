import { Speciality } from "./speciality.model";

export class Professional {
  constructor(
    public id?: number,
    public name?: string,
    public phone?: string,
    public speciality?: Speciality,
    public accepted_volunteer_terms?: boolean,
    public enabled?: boolean,
    public approved?: boolean
  ) { }
}

// Objetos vem diferentes do get e do post, então tive que fazer dois objetos diferentes
export class ProfessionalPOST {
  constructor(
    public id?: number,
    public name?: string,
    public phone?: string,
    public speciality_id?: number,
    public accepted_volunteer_terms?: boolean,
    public approved?: boolean
  ) { }

  transformObjectToEdit(professional: Professional) {
    this.id = professional.id;
    this.name = professional.name;
    this.phone = professional.phone;
    this.speciality_id = professional.speciality?.id;
    this.accepted_volunteer_terms = professional.accepted_volunteer_terms;
    this.approved = professional.approved;
  }
}