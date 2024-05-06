export class Campaign {
    constructor(
      public id?: number,
      public name?: string,
      public startDate?: Date,
      public endDate?: Date,
      public description?: string
    ) { }
  }

  export class CampaignPOST {
    constructor(
      public id?: number,
      public name?: string,
      public startDate?: Date,
      public endDate?: Date,
      public description?: string
    ) { }
  
    transformObjectToEdit(campaign: Campaign) {
      this.id = campaign.id;
      this.name = campaign.name;
      this.startDate = campaign.startDate;
      this.endDate = campaign.endDate;
      this.description = campaign.description;
    }
  }