import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { Beneficiary, BeneficiaryPOST, SwalFacade } from 'src/app/shared';
import { EvaluationServiceService } from 'src/app/volunteer/services/evaluation-service.service';
import { ApproveBeneficiaryComponent } from '../approve-beneficiary/approve-beneficiary.component';

@Component({
  selector: 'app-pending-evaluations',
  templateUrl: './pending-evaluations.component.html',
  styleUrls: ['./pending-evaluations.component.css']
})
export class PendingEvaluationsComponent implements OnInit {

  beneficiaries!: Beneficiary[];
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private evaluationService: EvaluationServiceService, private router: Router) { }

  ngOnInit(): void {
    // this.beneficiaries = []; // Array vazio para não dar erro no console
    this.listPendingBeneficiaries(false) // Lista inicialmente os profissionais pendentes
    this.subscription = this.evaluationService.refreshPage$.subscribe(() => {
      this.listPendingBeneficiaries(false); // Lista os beneficiados novamente para refletir as atualizações.
    })
  }

  ngOnDestroy(): void {
    // Cancela a subscrição para evitar vazamentos de memória.
    this.subscription?.unsubscribe();
  }

  /**
   * @description Lista as beneficiadas pendentes
   * @param isFiltering boolean que indica se a listagem será filtrada ou não
   */
  listPendingBeneficiaries(isFiltering: boolean) {
    this.isLoading = true; // Flag de carregamento
    this.evaluationService.listPendingBeneficiaries().subscribe({
      next: (response) => {
        this.beneficiaries = response
        // Ordena por nome crescente
        this.beneficiaries.sort((a, b) => (a.user?.name ?? '').localeCompare(b.user?.name ?? ''))
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => {
        if (isFiltering) {
          this.beneficiaries = this.beneficiaries.filter(
            (beneficiary: Beneficiary) => {
              // Asegura que name é uma string antes de chamar métodos de string
              return beneficiary.user?.name ? beneficiary.user?.name.toLowerCase().includes(this.filter.toLowerCase()) : false;
            }
          );
        }
        this.isLoading = false;
      }
    })
  }

  /**
   * @description Abre um componente modal para aprovar uma beneficiada
   * @param beneficiary O objeto  da beneficiada
   */
  approveBeneficiary(beneficiary: Beneficiary) {
    this.modalService.open(ApproveBeneficiaryComponent, { size: 'xl' })
      .componentInstance.beneficiary = beneficiary;  // Passando a beneficiada
  }

  /**
   * @description Navega para a rota de inspeção e verificar os dados da beneficiada
   * @param beneficiary objeto da beneficiada para ir como parâmetro na rota
   */
  inspectBeneficiary(beneficiary: Beneficiary) {
    this.router.navigate(['/voluntaria/beneficiadas/inspecionar', beneficiary.id])
  }

  /**
   * @description Verifica se o usuário está filtrando dados e chama os métodos
   * @param event Um evento do input
   */
  filterBeneficiary(event: Event) {
    if (event != undefined) {
      this.beneficiaries = []; // Esvazia o array

      // A ideia tem que ser se tiver string então filtrar 
      if (this.filter != '') {
        this.listPendingBeneficiaries(true)
      } else {
        // se não tiver então a gente filtra tudo
        this.listPendingBeneficiaries(false);
      }
    }
  }
}
