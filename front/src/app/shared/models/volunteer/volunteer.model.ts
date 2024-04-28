import { Group } from "./group.model";

export class Volunteer {
  constructor(
    public id?: number,
    public name?: string,
    public phone?: string,
    public enabled?: boolean,
    public group?: Group,
    
  ) { }
}

// Objetos vem diferentes do get e do post, então tive que fazer dois objetos diferentes
export class VolunteerPOST {
  password: any;
  constructor(
    public id?: number,
    public name?: string,
    public phone?: string,
    public group_id?: number,
   
  ) { }

  transformObjectToEdit(volunteer: Volunteer) {
    this.id = volunteer.id;
    this.name = volunteer.name;
    this.phone = volunteer.phone;
    this.group_id = volunteer.group?.id;
  }
}