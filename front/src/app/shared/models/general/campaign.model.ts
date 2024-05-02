export class Campaign {
  constructor(
    public id?: number,
    public name?: string,
    public start_date?: Date,
    public end_date?: Date,
    public description?: string,
    public external_link?: string
  ) { }
}
