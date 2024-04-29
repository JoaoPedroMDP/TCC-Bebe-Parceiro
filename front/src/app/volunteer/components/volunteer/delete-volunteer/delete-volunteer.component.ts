import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { Volunteer } from 'src/app/shared/models/volunteer/volunteer.model';
import { VolunteerService } from 'src/app/volunteer/services/volunteer.service';

@Component({
  selector: 'app-delete-volunteer',
  templateUrl: './delete-volunteer.component.html',
  styleUrls: ['./delete-volunteer.component.css']
})
export class DeleteVolunteerComponent implements OnInit {

  @Input() volunteer!: Volunteer;

  constructor(public activeModal: NgbActiveModal, public volunteerService: VolunteerService) { }

  ngOnInit(): void {
  }

  /**
   * @description Executa o método deleteVolunteer() do volunteerService e retorna uma mensagem 
   * de sucesso ou erro a depender do resultado da operação
   */
  deleteVolunteer() {
    this.volunteerService.deleteVolunteer(this.volunteer.id!).subscribe({
      next: () => {
        this.activeModal.close();
        SwalFacade.success("Voluntária", `${this.volunteer.user?.name}  excluída com sucesso!`)
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", `Não foi possível fazer excluir o profssional: ${e}`)
    })
  }

  
}
