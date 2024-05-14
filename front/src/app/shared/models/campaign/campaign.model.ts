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

  export class CampaignPOST {
    constructor(
      public id?: number,
      public name?: string,
      public start_date?: Date,
      public end_date?: Date,
      public description?: string,
      public external_link?: string
    ) { }
  
    transformObjectToEdit(campaign: Campaign) {
      this.id = campaign.id;
      this.name = campaign.name;
      this.start_date = campaign.start_date;
      this.end_date= campaign.end_date;
      this.description = campaign.description;
      this.external_link = campaign.external_link;
      
    }
  }