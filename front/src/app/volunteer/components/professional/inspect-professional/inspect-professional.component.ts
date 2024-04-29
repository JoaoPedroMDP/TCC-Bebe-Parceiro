import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Professional } from 'src/app/shared/models/professional';
import { DeleteProfessionalComponent } from '../delete-professional/delete-professional.component';
import { ApproveRefuseProfessionalComponent } from '../approve-refuse-professional/approve-refuse-professional.component';
import { CreateEditProfessionalComponent } from '../create-edit-professional/create-edit-professional.component';

@Component({
  selector: 'app-inspect-professional',
  templateUrl: './inspect-professional.component.html',
  styleUrls: ['./inspect-professional.component.css']
})
export class InspectProfessionalComponent implements OnInit {

  @Input() professional!: Professional;
  @Input() isProfessionalApproved!: boolean;

  constructor(public activeModal: NgbActiveModal, public modalService: NgbModal) { }

  ngOnInit(): void {
  }

  /**
   * @description Abre o modal de edição
   * @param professional objeto do profissional para ir como variavel no componente
   */
  editProfessional(professional: Professional) {
    this.activeModal.close(); // Fecha o modal atual de visualização
    let modalRef = this.modalService.open(CreateEditProfessionalComponent, { size: 'xl' })
    modalRef.componentInstance.professional = professional;  // Passando o profissional
    modalRef.componentInstance.editMode = true;          // Passando o modo de edição
  }

  /**
   * @description Abre o modal de exclusão
   * @param professional objeto do profissional para ir como variavel no componente
   */
  deleteProfessional(professional: Professional) {
    this.activeModal.close(); // Fecha o modal atual de visualização
    this.modalService.open(
      DeleteProfessionalComponent, { size: 'xl' }
    ).componentInstance.professional = professional;
  }

  /**
   * @description Abre um componente modal para aprovar um profissional
   * @param professional O objeto do profissional
   */
  approveProfessional(professional: Professional) {
    this.activeModal.close(); // Fecha o modal atual de visualização
    let modalRef = this.modalService.open(ApproveRefuseProfessionalComponent, { size: 'xl' });
    modalRef.componentInstance.professional = professional;  // Passando o profissional
    modalRef.componentInstance.isApproving = true;        // Passando a flag de aprovação
  }

  /**
   * @description Abre um componente modal para rejeitar um profissional
   * @param professional O objeto do profissional
   */
  refuseProfessional(professional: Professional) {
    this.activeModal.close(); // Fecha o modal atual de visualização
    let modalRef = this.modalService.open(ApproveRefuseProfessionalComponent, { size: 'xl' });
    modalRef.componentInstance.professional = professional;  // Passando o profissional
    modalRef.componentInstance.isApproving = false;        // Passando a flag de remoção
  }
}
