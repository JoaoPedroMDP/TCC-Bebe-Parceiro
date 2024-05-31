import { Component, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { AppointmentPOST, Beneficiary, Professional, ProfessionalService, Speciality, SwalFacade, VolunteerService } from 'src/app/shared';
import { AppointmentService } from 'src/app/volunteer/services/appointment.service';
import { SpecialityService } from 'src/app/volunteer/services/speciality.service';

@Component({
  selector: 'app-create-appointment',
  templateUrl: './create-appointment.component.html',
  styleUrls: ['./create-appointment.component.css']
})
export class CreateAppointmentComponent implements OnInit {

  appointmentPOST!: AppointmentPOST;
  professionals!: Professional[];
  specialities!: Speciality[];
  beneficiaries!: Beneficiary[];

  constructor(public activeModal: NgbActiveModal,
    private professionalService: ProfessionalService,
    private appointmentService: AppointmentService,
    private specialityService: SpecialityService,
    private volunteerService: VolunteerService
  ) { }

  ngOnInit(): void {
    this.appointmentPOST = new AppointmentPOST();
    this.listBeneficiaries();
    this.listSpecialities();
  }

  /**
   * @description Salva um atendimento
   */
  saveAppointment() {
    console.log(this.appointmentPOST);
    this.appointmentService.createAppointment(this.appointmentPOST).subscribe({
      next: () => SwalFacade.success("Atendimento criado com sucesso!"),
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.activeModal.close()
    });
  }

  /**
   * @description Lista todas as beneficiadas no componente
   */
  listBeneficiaries() {
    this.volunteerService.listBeneficiary().subscribe({
      next: (response: Beneficiary[]) => {
        this.beneficiaries = response
        // Ordena por nome crescente
        this.beneficiaries.sort((a, b) => (a.user!.name ?? '').localeCompare(b.user!.name ?? ''))
      },
      error: (e) => SwalFacade.error("Ocorreu um erro ao listar beneficiadas!", e)
    })
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
}
