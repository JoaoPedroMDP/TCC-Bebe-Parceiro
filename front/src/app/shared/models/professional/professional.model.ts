export class Professional {
  constructor(
    public id?: number,
    public name?: string,
    public phone?: string,
    public speciality?: {
        id: number,
        name: string,
        enabled: boolean
    },
    public accepted_volunteer_terms?: boolean,
    public enabled?: boolean
  ) { }
}

// Objetos vem diferentes do get e do post, então tive que fazer dois objetos diferentes
export class ProfessionalPost {
  constructor(
    public name?: string,
    public phone?: string,
    public speciality_id?: number,
    public accepted_volunteer_terms?: boolean
  ) { }
}