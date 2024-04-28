import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Group} from 'src/app/shared/models/';
import { VolunteerPOST} from 'src/app/shared/models/volunteer/volunteer.model';
import { SwalFacade} from 'src/app/shared';
import { VolunteerService } from 'src/app/volunteer/services/volunteer.service';
import { GroupService } from 'src/app/volunteer/services/group.service';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-edit-volunteer',
  templateUrl: './edit-volunteer.component.html',
  styleUrls: ['./edit-volunteer.component.css']
})
export class EditVolunteerComponent implements OnInit {
  @ViewChild('form') form!: NgForm;
  volunteer!: VolunteerPOST;
  @Input() editMode!: boolean;
  groups!: Group[];
  groupsService: any;

  constructor(public activeModal: NgbActiveModal, 
    private volunteerService: VolunteerService, 
    private groupService: GroupService) { }

  ngOnInit(): void {
    this.listGroups();
  }

  /**
   * @description Verifica a variável editMode e caso verdadeira atualiza o profissional, 
   * caso contrário salva como um novo profissional
   */
  save() {
    if (this.editMode) {
      this.volunteerService.editVolunteer(this.volunteer.id!, this.volunteer).subscribe({
        next: () => SwalFacade.success("Sucesso!", `${this.volunteer.name} foi atualizado com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      });
    } else {
      this.volunteerService.createVolunteer(this.volunteer).subscribe({
        next: () => SwalFacade.success("Sucesso!", `${this.volunteer.name} foi criado com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      });
    }
    this.activeModal.close();
  }

  /**
   * @description Lista as especialidades do profissional para realizar o cadastro
   */
  listGroups() {
    this.groupsService.listGroups().subscribe({
      next: (data: Group[]) => {
        if (data == null) {
          this.groups = [];
        } else {
          this.groups = data;
        }
      },
      error: (e: string | undefined) => SwalFacade.error('Erro ao listar os dados de Grupos', e)
    })
  }

  /**
   * @description Fecha a janela modal e chama o Observable de atualização
   */
  fechar() {
    this.activeModal.close();
    this.volunteerService.refreshPage$.next();
  }
}
