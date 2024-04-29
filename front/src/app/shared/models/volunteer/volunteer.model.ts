import { Groups_id } from "./group.model";
import { City,  User } from "../index";

export class Volunteer {
 
  constructor(
    public user?: User,
    public id?: number,
    public name?: string,
    public email?: string,
    public phone?: string,
    public city?: City,
    public enabled?: boolean,
    public groups_id?: Groups_id[],  
  ) { }
}

// Objetos vem diferentes do get e do post, então tive que fazer dois objetos diferentes
export class VolunteerPOST {
  constructor(
    public id?: number,
    public name?: string,
    public email?: string,
    public password?: string,
    public phone?: string,
    public groups_id?: Groups_id[],
    public city_id?: number,
   
  ) { }

  transformObjectToEdit(volunteer: Volunteer) {
    this.id = volunteer.id;
    this.name = volunteer.user?.name;
    this.phone = volunteer.user?.phone;
    this.email = volunteer.user?.email;
    this.groups_id = volunteer.groups_id;
    this.city_id = volunteer.city?.id;
  }
}