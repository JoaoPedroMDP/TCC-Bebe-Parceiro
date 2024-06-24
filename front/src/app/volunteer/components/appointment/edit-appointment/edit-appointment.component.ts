import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { AppointmentPOST, Beneficiary, Professional, ProfessionalService, Speciality, Status, SwalFacade, VolunteerService } from 'src/app/shared';
import { AppointmentService } from 'src/app/volunteer/services/appointment.service';
import { SpecialityService } from 'src/app/volunteer/services/speciality.service';


@Component({
  selector: 'app-edit-appointment',
  templateUrl: './edit-appointment.component.html',
  styleUrls: ['./edit-appointment.component.css']
})
export class EditAppointmentComponent implements OnInit {

  @Input() appointmentPOST!: AppointmentPOST;
  @Input() beneficiaryName!: string;
  @Input() isAppointmentClosed!: boolean;

  professionals!: Professional[];
  specialities!: Speciality[];

  constructor(public activeModal: NgbActiveModal,
    private professionalService: ProfessionalService,
    private appointmentService: AppointmentService,
    private specialityService: SpecialityService
  ) { }

  ngOnInit(): void {
    let auxProfessional = this.appointmentPOST.professional_id;
    this.listSpecialities();
    this.listProfessionals();
    this.appointmentPOST.professional_id = auxProfessional;
  }

  /**
   * @description Salva um atendimento
   */
  editAppointment(action?: string) {
    this.appointmentPOST.datetime = new Date();
    this.appointmentService.editAppointment(this.appointmentPOST.id!, this.appointmentPOST).subscribe({
      next: () => SwalFacade.success(`Atendimento ${action || 'editado'} com sucesso!`),
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.activeModal.close()
    });
  }

  /**
   * @description Lista todos os profissionais pela especialidade escolhida no atendimento
   */
  listProfessionals() {
    this.appointmentPOST.professional_id = undefined; // Mudou a especialidade, remove o profissional
    if (this.appointmentPOST.speciality_id) {
      this.professionalService.listProfessionalsBySpeciality(this.appointmentPOST.speciality_id).subscribe({
        next: (response) => {
          this.professionals = response
        },
        error: (e) => SwalFacade.error("Ocorreu um erro ao listar professionais!", e)
      })
    } else {
      SwalFacade.error("Ocorreu um erro!", "Não foi possível listar os profissionais pois não há especialidade")
    }
  }
  
  /**
   * @description Lista todas as especialidades no componente
   */
  listSpecialities() {
    this.specialityService.listSpecialities().subscribe({
      next: (response: Speciality[]) => {
        this.specialities = response
        // Ordena por nome crescente
        this.specialities.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''))
      },
      error: (e) => SwalFacade.error("Ocorreu um erro ao listar especialidades!", e)
    })
  }

  /**
   * @description Recupera o id do status Encerrado e atualiza o objeto atendimento
   */
  finishAppointment() {
    // Recupera o objeto com o nome de Encerrado e depois atribui o Id dele para o atendimento
    this.appointmentService.getClosedStatus().subscribe({
      next: (response: Status[]) => {
        // O método do service só traz um id, mas como ele sempre vem em array tem que pegar a primeira posição
        this.appointmentPOST.status_id = response[0].id;
        this.editAppointment('encerrado');
      },
    })
  }

  /**
   * @description Recupera o id do status Cancelado e atualiza o objeto atendimento
   */
  cancelAppointment() {
    // Recupera o objeto com o nome de Cancelado e depois atribui o Id dele para o atendimento
    this.appointmentService.getCanceledStatus().subscribe({
      next: (response: Status[]) => {
        // O método do service só traz um id, mas como ele sempre vem em array tem que pegar a primeira posição
        this.appointmentPOST.status_id = response[0].id;
        this.editAppointment('cancelado');
      },
    })
  }
}
