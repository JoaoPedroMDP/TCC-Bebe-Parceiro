import { Child, City, MaritalStatus, SocialProgram, User } from "../index";

export class BeneficiaryPOST {
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
    public social_programs?: SocialProgram[],
    public children?: Child[]
  ) { }
}

export class Beneficiary {
  constructor(
    public id?: number,
    public user?: User,
    public birth_date?: string,
    public child_count?: number,
    public monthly_familiar_income?: string,
    public has_disablement?: boolean,
    public marital_status?: MaritalStatus,
    public children?: Child[],
    public city?: City,
    public social_programs?: SocialProgram[],
    public created_at?: string
  ) { }
}