import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { Speciality } from 'src/app/shared/models/professional';
import { SpecialityService } from 'src/app/volunteer/services/speciality.service';

@Component({
  selector: 'app-create-edit-speciality',
  templateUrl: './create-edit-speciality.component.html',
  styleUrls: ['./create-edit-speciality.component.css']
})
export class CreateEditSpecialityComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  @Input() speciality!: Speciality;
  @Input() editMode: boolean = false;

  constructor(public activeModal: NgbActiveModal, private specialityService: SpecialityService) { }

  ngOnInit(): void {
  }

  /**
   * @description Verifica a variável editMode e caso verdadeira atualiza a especialidade, 
   * caso contrário salva como uma nova especialidade
   */
  save() {
    if (this.editMode) {
      this.specialityService.editSpeciality(this.speciality.id!, this.speciality).subscribe({
        next: () => SwalFacade.success("Sucesso!", `${this.speciality.name} foi atualizado com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      });
    } else {
      this.specialityService.createSpeciality(this.speciality).subscribe({
        next: () => SwalFacade.success("Sucesso!", `${this.speciality.name} foi criado com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      });
    }
    this.activeModal.close();
  }

  /**
   * @description Fecha a janela modal e chama o Observable de atualização
   */
  fechar() {
    this.activeModal.close();
    this.specialityService.refreshPage$.next();
  }
}
