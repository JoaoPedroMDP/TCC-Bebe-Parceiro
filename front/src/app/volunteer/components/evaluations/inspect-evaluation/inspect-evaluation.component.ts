import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Appointment, SwalFacade } from 'src/app/shared';
import { EvaluationService } from 'src/app/volunteer/services/evaluation.service';

@Component({
  selector: 'app-inspect-evaluation',
  templateUrl: './inspect-evaluation.component.html',
  styleUrls: ['./inspect-evaluation.component.css']
})
export class InspectEvaluationComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  @Input() evaluation!: Appointment;
  description!: string;

  constructor(public activeModal: NgbActiveModal, private evaluationService: EvaluationService) { }

  ngOnInit(): void {}

  /**
   * @description Fecha a admissão aprovando a beneficiada
   */
  save() {
    this.evaluationService.closeEvaluation(this.evaluation.id!, this.description).subscribe({
      next: () => SwalFacade.success("Sucesso!", `${this.evaluation?.beneficiary?.user?.name} foi aprovada com sucesso!`),
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.activeModal.close()
    })
  }
}
