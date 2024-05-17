import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { BeneficiaryService } from 'src/app/beneficiary/services/beneficiary.service';
import { Campaign, SwalFacade } from 'src/app/shared';

@Component({
  selector: 'app-list-campaign',
  templateUrl: './list-campaign.component.html',
  styleUrls: ['./list-campaign.component.css']
})
export class ListCampaignComponent implements OnInit {

  campaigns: Campaign[] = [];
  isLoading: boolean = false;

  constructor(private beneficiaryService: BeneficiaryService, private router: Router) { }

  ngOnInit(): void {
    this.listCampaigns();
  }

  /**
   * @description Lista as campanhas que estão aberta e ordena elas 
   */
  listCampaigns() {
    this.isLoading = true; // Flag de carregamento
    this.beneficiaryService.listCampaigns().subscribe({
      next: (response) => {
        this.campaigns = response
        // Ordena pelo prazo da data final de forma crescente
        this.campaigns.sort((a, b) => {
          const dateA = new Date(a.end_date ?? 0);
          const dateB = new Date(b.end_date ?? 0);
          return dateA.getTime() - dateB.getTime();
        });
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.isLoading = false
    })
  }

  /**
   * @description Navega para a rota de inspeção e verificar os dados da campanha
   * @param campaign objeto da campanha para ir como parâmetro na rota
   */
  viewCampaign(campaign: Campaign) {
    this.router.navigate(['beneficiada/campanhas/inspecionar', campaign.id])
  }
}
