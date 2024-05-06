import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Campaign } from 'src/app/shared';
import { CampaignService } from 'src/app/volunteer/services/campaign.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { CreateEditCampaignComponent } from '../create-edit-campaign/create-edit-campaign.component';
import { DeleteCampaignComponent } from '../delete-campaign/delete-campaign.component';
import { InspectCampaignComponent } from '../inspect-campaign/inspect-campaign.component';
import { CampaignPOST } from 'src/app/shared/models/campaign/campaign.model';

@Component({
  selector: 'app-list-campaign',
  templateUrl: './list-campaign.component.html',
  styleUrls: ['./list-campaign.component.css']
})
export class ListCampaignComponent implements OnInit, OnDestroy {

  campaigns!: Campaign[];
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private campaignService: CampaignService) { }

  ngOnInit(): void {
    this.listCampaigns(false); // Lista inicialmente as campanhas
    this.subscription = this.campaignService.refreshPage$.subscribe(() => {
      this.listCampaigns(false); // Lista os campanhas novamente para refletir as atualizações.
    });
  }

  ngOnDestroy(): void {
    // Cancela a subscrição para evitar vazamentos de memória.
    this.subscription?.unsubscribe();
  }

  /**
   * @description Lista todos os profissionais no componente
   * @param isFiltering boolean que indica se a listagem será filtrada ou não
   */
  listCampaigns(isFiltering: boolean) {
    this.isLoading = true;
    this.campaignService.listCampaigns().subscribe({
      next: (response) => {
        this.campaigns = response
        // Ordena por nome crescente
        this.campaigns.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''))
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => {
        if (isFiltering) {
          this.campaigns = this.campaigns.filter(
            (campaign: Campaign) => {
              // Asegura que name é uma string antes de chamar métodos de string
              return campaign.name ? campaign.name.toLowerCase().includes(this.filter.toLowerCase()) : false;
            }
          );
        }
        this.isLoading = false;
      }
    })
  }

  /**
   * @description Verifica se o usuário está filtrando dados e chama os métodos
   * @param event Um evento do input
   */
  filterCampaign(event: Event) {
    if (event != undefined) {
      this.campaigns = []; // Esvazia o array

      // A ideia tem que ser se tiver string então filtrar 
      if (this.filter != '') {
        this.listCampaigns(true)
      } else {
        // se não tiver então a gente filtra tudo
        this.listCampaigns(false);
      }
    }
  }

  /**
   * @description Abre o modal de edição
   * @param campaign objeto da campanha para ir como variavel no componente
   */
  editCampaign(campaign: Campaign) {
    let modalRef = this.modalService.open(CreateEditCampaignComponent, { size: 'lg' });
    modalRef.componentInstance.campaign = campaign;
    modalRef.componentInstance.editMode = true;
  }

  /**
   * @description Abre o modal de exclusão
   * @param campaign objeto da campanha para ir como variavel no componente
   */
  deleteCampaign(campaign: Campaign) {
    let modalRef = this.modalService.open(DeleteCampaignComponent, { size: 'xl' });
    modalRef.componentInstance.campaign = campaign;
  }

  /**
   * @description Abre o modal de inspeção
   * @param campaign objeto da campanha para ir como variavel no componente
   */
  inspectCampaign(campaign: Campaign) {
    let modalRef = this.modalService.open(InspectCampaignComponent, { size: 'lg' });
    modalRef.componentInstance.campaign = campaign;
  }

  /**
   * @description Abre o modal de criação
   */
  newCampaign() {
    let modalRef = this.modalService.open(CreateEditCampaignComponent, { size: 'xl' });
    modalRef.componentInstance.campaign = new CampaignPOST();
    modalRef.componentInstance.editMode = false;
  }
}
