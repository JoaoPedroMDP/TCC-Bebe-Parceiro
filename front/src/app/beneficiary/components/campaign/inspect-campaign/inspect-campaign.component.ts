import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BeneficiaryService } from 'src/app/beneficiary/services/beneficiary.service';
import { Campaign, SwalFacade } from 'src/app/shared';

@Component({
  selector: 'app-inspect-campaign',
  templateUrl: './inspect-campaign.component.html',
  styleUrls: ['./inspect-campaign.component.css']
})
export class InspectCampaignComponent implements OnInit {

  campaign!: Campaign;

  constructor(private router: Router,
    private route: ActivatedRoute,
    private beneficiaryService: BeneficiaryService) { }

  ngOnInit(): void {
    // Inicializa um objeto vazio para evitar erros de undefined
    this.campaign = new Campaign();
    // Recupera o objeto da campanha através do ID presente na rota
    // Ou seja na url /campanhas/inspecionar/9 será recuperado o ID 9 
    // e irá buscar a campanha com esse ID e  mostrar os dados dela
    this.route.paramMap.subscribe(params => {
      const campaignId = Number(params.get('idCampanha'));
      if (campaignId) {
        this.beneficiaryService.findCampaign(campaignId).subscribe({
          next: (response) => this.campaign = response,
          error: (e) => {
            SwalFacade.error("Ocorreu um erro! Redirecionando para a listagem", e)
            this.router.navigate(['/beneficiada/campanhas'])
          }
        });
      }
    });
  }

}
