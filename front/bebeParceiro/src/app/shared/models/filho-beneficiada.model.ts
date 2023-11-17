export class FilhoBeneficiada {
  constructor (
    public name?: string,
    public birth_date?: Date,
    public child_count?: number,
    public email?: string,
    public has_disablement?: boolean,
    public marital_status_id?: any,
    public mothly_familiar_income?: number,
    public password?: string,
    public password_confirm?: string,
    public phone?: string
  ) { }
}
