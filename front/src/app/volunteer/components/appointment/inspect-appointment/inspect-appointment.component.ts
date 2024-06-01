import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Appointment, AppointmentPOST } from 'src/app/shared';
import { DeleteAppointmentComponent } from '../delete-appointment/delete-appointment.component';
import { EditAppointmentComponent } from '../edit-appointment/edit-appointment.component';

@Component({
  selector: 'app-inspect-appointment',
  templateUrl: './inspect-appointment.component.html',
  styleUrls: ['./inspect-appointment.component.css']
})
export class InspectAppointmentComponent implements OnInit {

  @Input() appointment!: Appointment;

  constructor(public activeModal: NgbActiveModal, private modalService: NgbModal) { }

  ngOnInit(): void {
  }

  /**
   * @description Abre o modal de edição
   */
  editAppointment() {
    this.activeModal.close();
    let appointmentPOST: AppointmentPOST = new AppointmentPOST();
    let isAppointmentClosed = this.appointment.status?.name == "Encerrado" || this.appointment.status?.name == "Cancelado" ? true : false;
    appointmentPOST.transformObjectToEdit(this.appointment)
    let modalRef = this.modalService.open(EditAppointmentComponent, { size: 'xl' })
    modalRef.componentInstance.appointmentPOST = appointmentPOST;  // Passando o atendimento
    modalRef.componentInstance.beneficiaryName = this.appointment.beneficiary?.user?.name;  // Passando a beneficiada
    modalRef.componentInstance.isAppointmentClosed = isAppointmentClosed; // variável boolean pra mostrar botões de encerrar ou cancelar atendimento
  }

  deleteAppointment() {
    this.activeModal.close();
    this.modalService.open(DeleteAppointmentComponent, { size: 'xl' })
      .componentInstance.appointment = this.appointment; // Passando o atendimento
  }

}
