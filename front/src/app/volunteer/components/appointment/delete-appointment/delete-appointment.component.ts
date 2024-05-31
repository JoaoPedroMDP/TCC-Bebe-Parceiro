import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Appointment, SwalFacade } from 'src/app/shared';
import { AppointmentService } from 'src/app/volunteer/services/appointment.service';

@Component({
  selector: 'app-delete-appointment',
  templateUrl: './delete-appointment.component.html',
  styleUrls: ['./delete-appointment.component.css']
})
export class DeleteAppointmentComponent implements OnInit {

  @Input() appointment!: Appointment;

  constructor(public activeModal: NgbActiveModal, private appointmentService: AppointmentService) { }

  ngOnInit(): void {
  }

  /**
   * @description Executa o método deleteAppointment() do appointmentService e retorna uma mensagem 
   * de sucesso ou erro a depender do resultado da operação.
   */
  deleteAppointment() {
    this.appointmentService.deleteAppointment(this.appointment.id!).subscribe({
      next: () => SwalFacade.success("Atendimento excluído", `Atendimento foi excluído com sucesso!`),
      error: (e) => SwalFacade.error("Ocorreu um erro!", `Não foi possível excluir o atendimento: ${e}`),
      complete: () => this.activeModal.close()
    })
  }
}
