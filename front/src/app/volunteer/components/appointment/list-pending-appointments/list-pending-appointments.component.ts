import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { Appointment, AppointmentPOST, Beneficiary, SwalFacade } from 'src/app/shared';
import { AppointmentService } from 'src/app/volunteer/services/appointment.service';
import { ApproveAppointmentComponent } from '../approve-appointment/approve-appointment.component';

@Component({
  selector: 'app-list-pending-appointments',
  templateUrl: './list-pending-appointments.component.html',
  styleUrls: ['./list-pending-appointments.component.css']
})
export class ListPendingAppointmentsComponent implements OnInit {

  appointments!: Appointment[];
  originalAppointments!: Appointment[];  // Armazena as trocas originais para aplicar filtros
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private appointmentService: AppointmentService, private router: Router) { }

  ngOnInit(): void {
    this.appointments = []; // Array vazio para não dar erro no console
    this.listPendingAppointments(); // Lista inicialmente os atendimentos pendentes
    this.subscription = this.appointmentService.refreshPage$.subscribe(() => {
      this.listPendingAppointments(); // Lista os atendimentos novamente para refletir as atualizações.
    })
  }

  ngOnDestroy(): void {
    // Cancela a subscrição para evitar vazamentos de memória.
    this.subscription?.unsubscribe();
  }

  /**
   * @description Lista os profissionais pendentes
   */
  listPendingAppointments() {
    this.isLoading = true; // Flag de carregamento
    this.appointmentService.listPendingAppointments().subscribe({
      next: (response: Appointment[]) => {
        this.originalAppointments = response;
        this.filterAppointment();
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.isLoading = false
    });
  }

  /**
   * @description Filtra os campos de beneficiada e especialidade pelo input inserido
   */
  filterAppointment() {
    if (this.filter) {
      const filterLower = this.filter.toLowerCase();
      this.appointments = this.originalAppointments.filter(appointment => (
        appointment.beneficiary?.user?.name?.toLowerCase().includes(filterLower) ||
        appointment.speciality?.name?.toLowerCase().includes(filterLower))
      );
    } else {
      this.appointments = [...this.originalAppointments]; // Retorna todos os appointments se não há filtro
    }
  }

  /**
   * @description Abre um componente modal para aprovar um atendimento
   * @param appointment O objeto do atendimento
   */
  approveAppointment(appointment: Appointment) {
    // Transforma em appointmentPOST para então abrir o componente de aprovação
    let appointmentPOST: AppointmentPOST = new AppointmentPOST();
    appointmentPOST.transformObjectToEdit(appointment)
    let modalRef = this.modalService.open(ApproveAppointmentComponent, { size: 'xl' })
    modalRef.componentInstance.appointmentPOST = appointmentPOST;  // Passando o atendimento
    modalRef.componentInstance.specialityName = appointment.speciality?.name;  // Passando a especialidade
    modalRef.componentInstance.beneficiaryName = appointment.beneficiary?.user?.name;  // Passando a beneficiada
  }

  /**
   * @description Navega para a rota de inspeção e verificar os dados da beneficiada
   * @param beneficiary objeto da beneficiada para ir como parâmetro na rota
   */
  inspectBeneficiary(beneficiary: Beneficiary) {
    this.router.navigate(['/voluntaria/beneficiadas/inspecionar', beneficiary.id])
  }

  /**
   * @description Abre um SwalFacade para recusar o atendimento
   * @param appointment O objeto do atendimento
   */
  refuseAppointment(appointment: Appointment) {
    let beneficiaryName = appointment.beneficiary?.user?.name
    SwalFacade.delete("Recusar atendimento", "Recusar", `O atendimento da beneficiada ${beneficiaryName} - ${appointment.speciality?.name} será recusado.`)
      .then((result) => {
        if (result.isConfirmed) {
          this.appointmentService.deleteAppointment(appointment.id!).subscribe({
            next: () => SwalFacade.success("Atendimento Recusado", `Atendimento de ${beneficiaryName} foi recusado com sucesso!`),
            error: (e) => SwalFacade.error("Ocorreu um erro!", e)
          });
        }
      })
  }
}
