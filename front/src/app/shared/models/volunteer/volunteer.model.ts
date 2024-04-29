import { Group_ids } from "./group.model";
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
    public group_ids?: Group_ids[],  
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
    public group_ids?: Group_ids[],
    public city_id?: number,
   
  ) { }

  transformObjectToEdit(volunteer: Volunteer) {
    this.id = volunteer.id;
    this.name = volunteer.user?.name;
    this.phone = volunteer.user?.phone;
    this.email = volunteer.user?.email;
    this.group_ids = volunteer.group_ids;
    this.city_id = volunteer.city?.id;
  }
}