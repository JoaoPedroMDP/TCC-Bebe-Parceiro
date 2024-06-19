import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Beneficiary, SwalFacade, Volunteer, VolunteerService } from 'src/app/shared';
import { EvaluationService } from 'src/app/volunteer/services/evaluation.service';

@Component({
  selector: 'app-approve-beneficiary',
  templateUrl: './approve-beneficiary.component.html',
  styleUrls: ['./approve-beneficiary.component.css']
})
export class ApproveBeneficiaryComponent implements OnInit {

  @Input() beneficiary!: Beneficiary;
  datetime!: Date;
  volunteers!: Volunteer[];
  volunteer_id!: number;

  constructor(public activeModal: NgbActiveModal, private evaluationService: EvaluationService) { }

  ngOnInit(): void {
    this.listVolunteers();
  }

  /**
   * @description Cria um atendimento para a beneficiada, esse irá ser listado nas admissões pendentes
   * e lá ele poderá ser fechado para aprovar a beneficiada
   */
  save() {
    this.evaluationService.createEvaluationBeneficiary(this.beneficiary.id!, this.datetime, this.volunteer_id).subscribe({
      next: () => SwalFacade.success("Sucesso!", `${this.beneficiary.user?.name} foi aprovada com sucesso!`),
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.activeModal.close()
    });
  }

  listVolunteers(){
    this.evaluationService.listVolunteersEvaluators().subscribe({
      next: (data: Volunteer[]) => this.volunteers = data,
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
    })
  }
}
