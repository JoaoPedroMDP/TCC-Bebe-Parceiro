import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { CampaignPOST } from 'src/app/shared/models/campaign/campaign.model';
import { CampaignService } from 'src/app/volunteer/services/campaign.service';





@Component({
  selector: 'app-create-edit-campaign',
  templateUrl: './create-edit-campaign.component.html',
  styleUrls: ['./create-edit-campaign.component.css']
})
export class CreateEditCampaignComponent implements OnInit {

  @Input() campaign!: CampaignPOST;
  @Input() editMode!: boolean;

  constructor(public activeModal: NgbActiveModal, private campaignService: CampaignService) { }

  ngOnInit(): void {}

  save() {
    if (this.editMode) {
      this.campaignService.editCampaign(this.campaign.id!, this.campaign).subscribe({
        next: () => SwalFacade.success("Sucesso!", `${this.campaign.name} foi atualizado com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      });
    } else {
      this.campaignService.createCampaign(this.campaign).subscribe({
        next: () => SwalFacade.success("Sucesso!", `${this.campaign.name} foi criado com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      });
    }
    this.activeModal.close();
  }

  close() {
    this.activeModal.close();
  }
}
