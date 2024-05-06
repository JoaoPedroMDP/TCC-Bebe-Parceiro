import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Volunteer, VolunteerPOST } from 'src/app/shared/models/volunteer/volunteer.model';
import { DeleteVolunteerComponent } from '../delete-volunteer/delete-volunteer.component';
import { ActivatedRoute, Router } from '@angular/router';
import { SwalFacade, VolunteerService } from 'src/app/shared';
import { CreateEditVolunteerComponent } from '../create-edit-volunteer/create-edit-volunteer.component';




@Component({
  selector: 'app-inspect-volunteer',
  templateUrl: './inspect-volunteer.component.html',
  styleUrls: ['./inspect-volunteer.component.css']
})
export class InspectVolunteerComponent implements OnInit {

  @Input() volunteer!: Volunteer;
  
  
  constructor(public activeModal: NgbActiveModal, public modalService: NgbModal) { }

  ngOnInit(): void {

  }

  /**
   * @description Abre o modal de edição
   * @param volunteer objeto da voluntária para ir como variavel no componente
   */
  editVolunteer(volunteer: Volunteer) {
    let volunteerPOST = new VolunteerPOST();
    volunteerPOST.transformObjectToEdit(volunteer);
    let modalRef = this.modalService.open(CreateEditVolunteerComponent, { size: 'xl' })
    modalRef.componentInstance.volunteer = volunteerPOST;  // Passando o voluntária
    modalRef.componentInstance.editMode = true;          // Passando o modo de edição
  }


  /**
   * @description Abre o modal de exclusão
   * @param volunteer objeto da voluntária para ir como variavel no componente
   */
  deleteVolunteer(volunteer: Volunteer) {
    this.activeModal.close(); // Fecha o modal atual de visualização
    this.modalService.open(
      DeleteVolunteerComponent, { size: 'xl' }
    ).componentInstance.volunteer = volunteer;
  }

}
