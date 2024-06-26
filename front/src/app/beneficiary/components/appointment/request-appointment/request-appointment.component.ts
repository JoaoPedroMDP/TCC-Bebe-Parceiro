import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { AppointmentPOST, Speciality, SwalFacade } from 'src/app/shared';
import { SpecialityService } from 'src/app/volunteer/services/speciality.service';
import { BeneficiaryService } from 'src/app/beneficiary/services/beneficiary.service';
import { AuthService } from 'src/app/auth';

@Component({
  selector: 'app-request-appointment',
  templateUrl: './request-appointment.component.html',
  styleUrls: ['./request-appointment.component.css']
})
export class RequestAppointmentComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  appointment!: AppointmentPOST;
  showSuccess!: boolean;

  specialities!: Speciality[];

  constructor(public activeModal: NgbActiveModal,
    private beneficiaryService: BeneficiaryService,
    private specialityService: SpecialityService,
    private authService: AuthService,
  ) { }

  ngOnInit(): void {
    this.specialities = []; // Array vazio para não dar erro de undefined
    this.appointment = new AppointmentPOST();
    this.appointment.beneficiary_id = this.authService.getUser().person_id; // Id da beneficiada
    this.listSpecialities();
  }

  /**
   * @description Cria um atendimento para a beneficiada com a especialidade escolhida
   */
  requestAppointment() {
    if (this.appointment.speciality_id) {
      this.beneficiaryService.createAppointment(this.appointment).subscribe({
        next: () => SwalFacade.success("Atendimento solicitado com sucesso", "Em breve entraremos em contato"),
        error: (e) => SwalFacade.error("Erro ao soliciitar o atendimento!", e),
        complete: () => this.showSuccess = !this.showSuccess
      });
    } else {
      SwalFacade.alert("Não foi possível solicitar o atendimento!", "Preencha os campos obrigatórios e tente novamente");
    }
  }

  /**
   * @description Lista as especialidades do profissional 
   */
  listSpecialities() {
    this.specialityService.listSpecialities().subscribe({
      next: (data: Speciality[]) => {
        if (data == null) {
          this.specialities = [];
        } else {
          this.specialities = data;
        }
      },
      error: (e) => SwalFacade.error('Erro ao listar os dados de Especialidades', e)
    })
  }

  /**
   * @description Fecha a janela modal e chama o Observable de atualização
   */
  close() {
    this.activeModal.close();
    this.beneficiaryService.refreshPage$.next();
  }
}



