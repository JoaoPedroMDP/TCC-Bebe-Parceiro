import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Beneficiary, SwalFacade } from 'src/app/shared';
import { EvaluationServiceService } from 'src/app/volunteer/services/evaluation-service.service';

@Component({
  selector: 'app-approve-beneficiary',
  templateUrl: './approve-beneficiary.component.html',
  styleUrls: ['./approve-beneficiary.component.css']
})
export class ApproveBeneficiaryComponent implements OnInit {

  @Input() beneficiary!: Beneficiary;
  datetime!: Date;

  constructor(public activeModal: NgbActiveModal, private evaluationService: EvaluationServiceService) { }

  ngOnInit(): void {
  }

  /**
   * @description Aprova uma beneficiada
   */
  save() {
    this.evaluationService.approveBeneficiary(this.beneficiary.id!, this.datetime).subscribe({
      next: () => SwalFacade.success("Sucesso!", `${this.beneficiary.user?.name} foi aprovada com sucesso!`),
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.activeModal.close()
    });
  }
}
