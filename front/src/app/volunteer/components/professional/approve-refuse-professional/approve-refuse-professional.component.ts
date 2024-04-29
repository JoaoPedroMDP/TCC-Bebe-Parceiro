import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { Professional } from 'src/app/shared/models/professional';
import { ProfessionalService } from 'src/app/volunteer/services/professional.service';

@Component({
  selector: 'app-approve-refuse-professional',
  templateUrl: './approve-refuse-professional.component.html',
  styleUrls: ['./approve-refuse-professional.component.css']
})
export class ApproveRefuseProfessionalComponent implements OnInit {

  @Input() professional!: Professional;
  @Input() isApproving!: boolean;

  constructor(public activeModal: NgbActiveModal, private professionalService: ProfessionalService) { }

  ngOnInit(): void {
  }

  /**
   * @description altera o atributo approved para true e depois chama o metodo editProfessional() do service
   */
  approveProfessional() {
    this.professional.approved = true; // Foi aprovado
    this.professionalService.editProfessional(this.professional.id!, this.professional).subscribe({
      next: () => SwalFacade.success("Profissional aprovado com sucesso!", `${this.professional.name} foi aprovado!`),
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.activeModal.close()
    });
  }

  /**
   * @description Chama o metodo deleteProfessional() do service para remover o profissional
   */
  refuseProfessional() {
    this.professionalService.deleteProfessional(this.professional.id!).subscribe({
      next: () => SwalFacade.success("Profissional removido com sucesso!", `${this.professional.name} foi removido!`),
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.activeModal.close()
    });
  }
}
