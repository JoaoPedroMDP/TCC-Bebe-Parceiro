
import { City,  User } from "../index";


export class Volunteer {
 
  constructor(
    public id?: number,
    public user?: User,
    public city?: City,
   
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
    public group_ids?: number[],
    public city_id?: number,
   
  ) { }

  transformObjectToEdit(volunteer: Volunteer) {
    this.id = volunteer.id;
    this.name = volunteer.user?.name;
    this.phone = volunteer.user?.phone;
    this.email = volunteer.user?.email;
    this.group_ids = volunteer.user?.groups
                            ?.map(group => group.id)
                            .filter(
                                (id): id is number => id !== undefined
                            ) || [];
    this.city_id = volunteer.city?.id;
  }
}