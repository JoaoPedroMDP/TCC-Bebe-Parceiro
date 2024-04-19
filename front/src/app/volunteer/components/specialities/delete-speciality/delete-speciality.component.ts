import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { Speciality } from 'src/app/shared/models/professional';
import { SpecialityService } from 'src/app/volunteer/services/speciality.service';

@Component({
  selector: 'app-delete-speciality',
  templateUrl: './delete-speciality.component.html',
  styleUrls: ['./delete-speciality.component.css']
})
export class DeleteSpecialityComponent implements OnInit {

  @Input() speciality!: Speciality;

  constructor(public activeModal: NgbActiveModal, public specialityService: SpecialityService) { }

  ngOnInit(): void { }

  /**
   * @description Tenta excluir a especialidade e retorna uma mensagem 
   * de sucesso ou erro a depender do resultado da operação
   */
  deleteSpeciality() {
    this.specialityService.deleteSpeciality(this.speciality.id!).subscribe({
      next: () => {
        this.activeModal.close();
        SwalFacade.success("Especialidade excluída", `${this.speciality.name} foi excluída com sucesso!`)
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e)
    })
  }

}
