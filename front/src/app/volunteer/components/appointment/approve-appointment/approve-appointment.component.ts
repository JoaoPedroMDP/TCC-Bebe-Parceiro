import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { AppointmentPOST, Professional, ProfessionalService, Status, SwalFacade } from 'src/app/shared';
import { AppointmentService } from 'src/app/volunteer/services/appointment.service';

@Component({
  selector: 'app-approve-appointment',
  templateUrl: './approve-appointment.component.html',
  styleUrls: ['./approve-appointment.component.css']
})
export class ApproveAppointmentComponent implements OnInit {

  @Input() appointmentPOST!: AppointmentPOST;
  @Input() specialityName!: string;
  @Input() beneficiaryName!: string;
  professionals!: Professional[];

  constructor(public activeModal: NgbActiveModal,
    private professionalService: ProfessionalService,
    private appointmentService: AppointmentService
  ) { }

  ngOnInit(): void {
    this.listProfessionals();
    // Recupera o objeto com o nome de Aprovado e depois atribui o Id dele para o atendimento
    this.appointmentService.getApprovedStatus().subscribe({
      next: (response: Status[]) => {
        // O método do service só traz um id, mas como ele sempre vem em array tem que pegar a primeira posição
        this.appointmentPOST.status_id = response[0].id; 
        // Por algum motivo o backend pede o datetime, então eu envio a data de hoje
        this.appointmentPOST.datetime = new Date();
      },
    })
  }

  /**
   * @description Aprova o atendimento da beneficiada e atualiza o objeto fazendo um patch
   */
  approveAppointment() {
    this.appointmentService.editAppointment(this.appointmentPOST.id!, this.appointmentPOST).subscribe({
      next: () => SwalFacade.success("Atendimento aprovado com sucesso!", `Atendimento de ${this.beneficiaryName} foi aprovada!`),
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.activeModal.close()
    });
  }

  /**
   * @description Lista todos os profissionais pela especialidade escolhida no atendimento
   */
  listProfessionals() {
    if (this.appointmentPOST.speciality_id) {
      this.professionalService.listProfessionalsBySpeciality(this.appointmentPOST.speciality_id).subscribe({
        next: (response) => {
          this.professionals = response
        },
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      })
    } else {
      SwalFacade.error("Ocorreu um erro!", "Não foi possível listar os profissionais pois não há especialidade")
    }
  }
}
