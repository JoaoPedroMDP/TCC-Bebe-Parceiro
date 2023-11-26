import { Child, SocialProgram } from "./index";

export class Benefited {
  constructor(
    public id?: number,
    public name?: string,
    public birth_date?: Date,
    public child_count?: number,
    public email?: string,
    public has_disablement?: boolean,
    public marital_status_id?: any,
    public monthly_familiar_income?: number,
    public password?: string,
    public phone?: string,
    public city_id?: number,
    public access_code?: string,
    public socialProgram?: SocialProgram[],
    public children?: Child[]
  ) { }
}
