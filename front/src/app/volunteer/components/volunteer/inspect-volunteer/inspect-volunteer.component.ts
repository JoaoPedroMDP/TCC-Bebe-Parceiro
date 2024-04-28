import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Volunteer } from 'src/app/shared/models/volunteer/volunteer.model';
import { DeleteVolunteerComponent } from '../delete-volunteer/delete-volunteer.component';
import { EditVolunteerComponent } from '../edit-volunteer/edit-volunteer.component';


@Component({
  selector: 'app-inspect-volunteer',
  templateUrl: './inspect-volunteer.component.html',
  styleUrls: ['./inspect-volunteer.component.css']
})
export class InspectVolunteerComponent implements OnInit {

  @Input() volunteer!: Volunteer;
  @Input() isVolunteerApproved!: boolean;

  constructor(public activeModal: NgbActiveModal, public modalService: NgbModal) { }

  ngOnInit(): void {
  }

  /**
   * @description Abre o modal de edição
   * @param volunteer objeto do profissional para ir como variavel no componente
   */
  editVolunteer(volunteer: Volunteer) {
    this.activeModal.close(); // Fecha o modal atual de visualização
    let modalRef = this.modalService.open(EditVolunteerComponent, { size: 'xl' })
    modalRef.componentInstance.volunteer = Volunteer;  // Passando o profissional
    modalRef.componentInstance.editMode = true;          // Passando o modo de edição
  }

  /**
   * @description Abre o modal de exclusão
   * @param volunteer objeto do profissional para ir como variavel no componente
   */
  deleteVolunteer(volunteer: Volunteer) {
    this.activeModal.close(); // Fecha o modal atual de visualização
    this.modalService.open(
      DeleteVolunteerComponent, { size: 'xl' }
    ).componentInstance.volunteer = volunteer;
  }

}
