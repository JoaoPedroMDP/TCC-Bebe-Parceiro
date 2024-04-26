import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { Professional } from 'src/app/shared/models/professional';
import { ProfessionalService } from 'src/app/volunteer/services/professional.service';

@Component({
  selector: 'app-delete-professional',
  templateUrl: './delete-professional.component.html',
  styleUrls: ['./delete-professional.component.css']
})
export class DeleteProfessionalComponent implements OnInit {

  @Input() professional!: Professional;

  constructor(public activeModal: NgbActiveModal, public professionalService: ProfessionalService) { }

  ngOnInit(): void {
  }

  /**
   * @description Executa o método deleteProfessional() do professionalService e retorna uma mensagem 
   * de sucesso ou erro a depender do resultado da operação
   */
  deleteProfessional() {
    this.professionalService.deleteProfessional(this.professional.id!).subscribe({
      next: () => {
        this.activeModal.close();
        SwalFacade.success("Profissional excluído", `${this.professional?.name} foi excluído com sucesso!`)
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", `Não foi possível fazer excluir o profssional: ${e}`)
    })
  }
}
