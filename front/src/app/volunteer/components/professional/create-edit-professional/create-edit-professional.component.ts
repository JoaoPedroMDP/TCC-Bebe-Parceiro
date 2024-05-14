import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { ProfessionalPOST, Speciality } from 'src/app/shared/models/professional';
import { ProfessionalService } from 'src/app/volunteer/services/professional.service';
import { SpecialityService } from 'src/app/volunteer/services/speciality.service';

@Component({
  selector: 'app-create-edit-professional',
  templateUrl: './create-edit-professional.component.html',
  styleUrls: ['./create-edit-professional.component.css']
})
export class CreateEditProfessionalComponent implements OnInit {

  @Input() professional!: ProfessionalPOST;
  @Input() editMode!: boolean;
  specialities!: Speciality[];

  constructor(public activeModal: NgbActiveModal, 
    private professionalService: ProfessionalService, 
    private specialityService: SpecialityService) { }

  ngOnInit(): void {
    this.listSpecialities();
  }
 
  /**
   * @description Verifica a variável editMode e caso verdadeira atualiza o profissional, 
   * caso contrário salva como um novo profissional
   */
  save() {
    if (this.editMode) {
      this.professionalService.editProfessional(this.professional.id!, this.professional).subscribe({
        next: () => SwalFacade.success("Sucesso!", `${this.professional.name} foi atualizado com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      });
    } else {
      this.professional.accepted_volunteer_terms = true;
      this.professional.approved = true;
      this.professionalService.createProfessional(this.professional).subscribe({
        next: () => SwalFacade.success("Sucesso!", `${this.professional.name} foi criado com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      });
    }
    this.activeModal.close();
  }

  /**
   * @description Lista as especialidades do profissional para realizar o cadastro
   */
  listSpecialities() {
    this.specialityService.listSpecialities().subscribe({
      next: (data: Speciality[]) => {
        if (data == null) {
          this.specialities = [];
        } else {
          this.specialities = data;
        }
      },
      error: (e) => SwalFacade.error('Erro ao listar os dados de Especialidades', e)
    })
  }

  /**
   * @description Fecha a janela modal e chama o Observable de atualização
   */
  fechar() {
    this.activeModal.close();
    this.professionalService.refreshPage$.next();
  }
}
