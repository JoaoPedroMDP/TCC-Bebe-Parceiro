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

  transformObjectToEdit(beneficiary: Beneficiary) {
    this.id = beneficiary.id;
    this.name = beneficiary.user?.name;
    this.birth_date = beneficiary.birth_date;
    this.child_count = beneficiary.child_count;
    this.email = beneficiary.user?.email;
    this.has_disablement = beneficiary.has_disablement;
    this.marital_status_id = beneficiary.marital_status?.id;
    this.monthly_familiar_income = beneficiary.monthly_familiar_income;
    this.phone = beneficiary.user?.phone;
    this.city_id = beneficiary.city?.id;
    this.social_programs = beneficiary.social_programs;
    this.children = beneficiary.children;
  }
}

export class Beneficiary {
  constructor(
    public id?: number,
    public user?: User,
    public birth_date?: Date,
    public child_count?: number,
    public monthly_familiar_income?: number,
    public has_disablement?: boolean,
    public marital_status?: MaritalStatus,
    public children?: Child[],
    public city?: City,
    public social_programs?: SocialProgram[],
    public created_at?: string,
    public is_pregnant?: boolean
  ) { }
}