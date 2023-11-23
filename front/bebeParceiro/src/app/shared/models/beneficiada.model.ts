import { Children, SocialProgram } from "./index";

export class Beneficiada {
  constructor (
    public id?: number,
    public name?: string,
    public birth_date?: Date,
    public child_count?: number,
    public email?: string,
    public has_disablement?: boolean,
    public marital_status_id?: any,
    public mothly_familiar_income?: number,
    public password?: string,
    public phone?: string,
    public city_id?: number,
    public socialProgram?: SocialProgram[],
    public children?: Children[]
  ) { }
}
