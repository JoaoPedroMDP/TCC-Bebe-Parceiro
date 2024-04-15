import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Benefited, SwalFacade } from 'src/app/shared';
import { VolunteerService } from 'src/app/volunteer/services/volunteer.service';

@Component({
  selector: 'app-delete-beneficiary',
  templateUrl: './delete-beneficiary.component.html',
  styleUrls: ['./delete-beneficiary.component.css']
})
export class DeleteBeneficiaryComponent implements OnInit {

  @Input() benefited!: Benefited;

  constructor(public activeModal: NgbActiveModal, public volunteerService: VolunteerService) { }

  ngOnInit(): void {
  }

  /**
   * @description Executa o método deleteBenefited() do VolunteerService e retorna uma mensagem 
   * de sucesso ou erro a depender do resultado da operação
   */
  deleteBenefited() {
    this.volunteerService.deleteBenefited(this.benefited.id!).subscribe({
      next: () => {
        this.activeModal.close(),
        SwalFacade.success("Beneficiada excluída", `${this.benefited.name} foi excluída com sucesso!`)
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", `Não foi possível fazer excluir a beneficiada: ${e}`)
    })
  }

}
