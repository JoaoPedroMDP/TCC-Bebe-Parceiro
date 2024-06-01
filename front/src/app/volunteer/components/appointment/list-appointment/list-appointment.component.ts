import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Appointment, AppointmentPOST } from 'src/app/shared/models/appointment/appointment.model';
import { AppointmentService } from 'src/app/volunteer/services/appointment.service';
import { CreateAppointmentComponent, DeleteAppointmentComponent, EditAppointmentComponent, InspectAppointmentComponent } from '../index';

@Component({
  selector: 'app-list-appointment',
  templateUrl: './list-appointment.component.html',
  styleUrls: ['./list-appointment.component.css']
})
export class ListAppointmentComponent implements OnInit {

  appointments!: Appointment[];
  originalAppointments!: Appointment[];  // Armazena as trocas originais para aplicar filtros
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private appointmentService: AppointmentService) { }

  ngOnInit(): void {
    this.listAppointments() // Lista inicialmente os atendimentos pendentes
    this.subscription = this.appointmentService.refreshPage$.subscribe(() => {
      this.listAppointments(); // Lista os beneficiados novamente para refletir as atualizações.
    })
  }

  ngOnDestroy(): void {
    // Cancela a subscrição para evitar vazamentos de memória.
    this.subscription?.unsubscribe();
  }

  /**
   * @description Lista os atendimentos
   */
  listAppointments() {
    this.isLoading = true; // Flag de carregamento
    this.appointmentService.listAppointments().subscribe({
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
        appointment.speciality?.name?.toLowerCase().includes(filterLower) ||
        appointment.status?.name?.toLowerCase().includes(filterLower))
      );
    } else {
      this.appointments = [...this.originalAppointments]; // Retorna todos os appointments se não há filtro
    }
  }

  /**
 * @description Abre o modal de inspeção
 * @param appointment objeto do atendimento para ir como variavel no componente
 */
  inspectAppointment(appointment: Appointment) {
    let isAppointmentClosed = appointment.status?.name == "Encerrado" || appointment.status?.name == "Cancelado" ? true : false;
    let modalRef = this.modalService.open(InspectAppointmentComponent, { size: 'xl' })
    modalRef.componentInstance.appointment = appointment; // Passando o atendimento
    modalRef.componentInstance.isAppointmentClosed = isAppointmentClosed; // variável boolean pra mostrar botões de encerrar ou cancelar atendimento
  }

  /**
   * @description  Abre o modal de criação
   */
  newAppointment() {
    this.modalService.open(CreateAppointmentComponent, { size: 'xl' });
  }

  /**
   * @description Abre o modal de edição
   * @param appointment objeto do profissional para ir como variavel no componente
   */
  editAppointment(appointment: Appointment) {
    let appointmentPOST: AppointmentPOST = new AppointmentPOST();
    let isAppointmentClosed = appointment.status?.name == "Encerrado" || appointment.status?.name == "Cancelado" ? true : false;
    appointmentPOST.transformObjectToEdit(appointment)
    let modalRef = this.modalService.open(EditAppointmentComponent, { size: 'xl' })
    modalRef.componentInstance.appointmentPOST = appointmentPOST;  // Passando o atendimento
    modalRef.componentInstance.beneficiaryName = appointment.beneficiary?.user?.name;  // Passando a beneficiada
    modalRef.componentInstance.isAppointmentClosed = isAppointmentClosed; // variável boolean pra mostrar botões de encerrar ou cancelar atendimento
  }

  /**
   * @description Abre o modal de exclusão
   * @param appointment objeto do atendimento para ir como variavel no componente
   */
  deleteAppointment(appointment: Appointment) {
    this.modalService.open(DeleteAppointmentComponent, { size: 'xl' })
      .componentInstance.appointment = appointment; // Passando o atendimento
  }
}
