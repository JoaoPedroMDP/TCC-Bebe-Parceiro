import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { Campaign } from 'src/app/shared/models/campaign';
import { CampaignService } from 'src/app/volunteer/services/campaign.service';

@Component({
  selector: 'app-delete-campaign',
  templateUrl: './delete-campaign.component.html',
  styleUrls: ['./delete-campaign.component.css']
})
export class DeleteCampaignComponent implements OnInit {

  @Input() campaign!: Campaign;

  constructor(public activeModal: NgbActiveModal, public campaignService: CampaignService) { }

  ngOnInit(): void {
  }

  /**
   * @description Executa o método deleteCampaign() do campaignService e retorna uma mensagem 
   * de sucesso ou erro a depender do resultado da operação
   */
  deleteCampaign() {
    this.campaignService.deleteCampaign(this.campaign.id!).subscribe({
      next: () => {
        this.activeModal.close();
        SwalFacade.success("Campanha Excluída", `${this.campaign?.name} foi excluída com sucesso!`)
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", `Não foi possível excluir a campanha: ${e}`)
    })
  }
}
