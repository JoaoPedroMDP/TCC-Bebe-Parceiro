import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Appointment, Beneficiary, SwalFacade } from 'src/app/shared';
import { EvaluationService } from 'src/app/volunteer/services/evaluation.service';
import { InspectEvaluationComponent } from '../inspect-evaluation/inspect-evaluation.component';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-assigned-evaluations',
  templateUrl: './assigned-evaluations.component.html',
  styleUrls: ['./assigned-evaluations.component.css']
})
export class AssignedEvaluationsComponent implements OnInit {

  evaluations!: Appointment[];
  isLoading!: boolean;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private evaluationService: EvaluationService) { }

  ngOnInit(): void {
    this.listEvaluations(); // Lista inicialmente as admissões
    this.subscription = this.evaluationService.refreshPage$.subscribe(() => {
      this.listEvaluations(); // Lista as admissões novamente para refletir as atualizações.
    })
  }

  /**
   * @description Lista todas as admissões designadas
   */
  listEvaluations() {
    this.isLoading = true;
    this.evaluationService.listAssignedEvaluations().subscribe({
      next: (data: Appointment[]) => {
        if (data != null) {
          this.evaluations = data;
          // Ordena por nome crescente
          this.evaluations.sort((a, b) => (a.beneficiary?.user?.name ?? '').localeCompare(b.beneficiary?.user?.name ?? ''))
        }
      },
      error: (e) => SwalFacade.error('Erro ao listar os dados de admissões', e),
      complete: () => this.isLoading = false
    })
  }

  /**
   * @description Abre um modal para inspecionar a admissão
   * @param evaluation A admissão para ser inspecionada
   */
  closeEvaluation(evaluation: Appointment) {
    this.modalService.open(
      InspectEvaluationComponent, { size: 'xl' }
    ).componentInstance.evaluation = evaluation;
  }

  /**
   * @description FAZER - Abre o prontuário da beneficiada
   * @param beneficiary A beneficiada
   */
  beneficiaryRecords(beneficiary: Beneficiary) {
    SwalFacade.alert("Hehe", "Não desenvolvido XD")
  }
}
