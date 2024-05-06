
import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { CreateEditCampaignComponent } from '../create-edit-campaign/create-edit-campaign.component';
import { Campaign } from 'src/app/shared/models/campaign';
import { CampaignService } from 'src/app/volunteer/services/campaign.service';
import { DeleteCampaignComponent } from '../delete-campaign/delete-campaign.component';

@Component({
  selector: 'app-inspect-campaign',
  templateUrl: './inspect-campaign.component.html',
  styleUrls: ['./inspect-campaign.component.css']
})
export class InspectCampaignComponent implements OnInit {

  @Input() campaign!: Campaign;

  constructor(public activeModal: NgbActiveModal, public modalService: NgbModal, public campaignService: CampaignService) { }

  ngOnInit(): void {
  }

  /**
   * @description Abre o modal de edição
   * @param campaign objeto da campanha para ir como variavel no componente
   */
  editCampaign(campaign: Campaign) {
    this.activeModal.close();
    let modalRef = this.modalService.open(CreateEditCampaignComponent, { size: 'xl' });
    modalRef.componentInstance.campaign = campaign;
    modalRef.componentInstance.editMode = true;
  }

  /**
   * @description Abre o modal de exclusão
   * @param campaign objeto da campanha para ir como variavel no componente
   */
  deleteCampaign(campaign: Campaign) {
    this.activeModal.close();
    let modalRef = this.modalService.open(DeleteCampaignComponent, { size: 'xl' });
    modalRef.componentInstance.campaign = campaign;
    modalRef.componentInstance.editMode = false;
  }
}

