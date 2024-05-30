import { Component, OnDestroy, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade, Appointment, AppointmentPOST } from 'src/app/shared';
import { BeneficiaryService } from '../../../services/beneficiary.service';
import { InspectAppointmentComponent } from '../inspect-appointment/inspect-appointment.component';
import { RequestAppointmentComponent } from '../request-appointment/request-appointment.component';


@Component({
  selector: 'app-list-appointment',
  templateUrl: './list-appointment.component.html',
  styleUrls: ['./list-appointment.component.css']
})
export class ListAppointmentComponent implements OnInit, OnDestroy {

  appointments!: Appointment[];
  originalAppointments!: Appointment[];  // Armazena as trocas originais para aplicar filtros
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private beneficiaryService: BeneficiaryService) { }

  ngOnInit(): void {
    this.listAppointments();  // Lista inicialmente as trocas
    this.subscription = this.beneficiaryService.refreshPage$.subscribe(() => {
      this.listAppointments(); // Lista as trocas novamente para refletir as atualizações.
    })
  }

  ngOnDestroy(): void {
    // Cancela a subscrição para evitar vazamentos de memória.
    this.subscription?.unsubscribe();
  }

  /**
   * @description Abre o modal de criação
   */
  newAppointment() {
    this.modalService.open(RequestAppointmentComponent, { size: 'xl' });
  }

  /**
   * @description lista os dados de atendimentos
   */
  listAppointments() {
    this.isLoading = true;
    this.beneficiaryService.listAppointments().subscribe({
      next: (response) => {
        this.originalAppointments = response;
        this.filterAppointment();
      },
      error: (e) => {
        SwalFacade.error("Ocorreu um erro!", e);
        this.isLoading = false;
      },
      complete: () => this.isLoading = false
    });
  }

  /**
   * @description Filtra os campos de nome, tamanho da roupa e status pelo input inserido
   */
  filterAppointment() {
    if (this.filter) {
      const filterLower = this.filter.toLowerCase();
      this.appointments = this.originalAppointments.filter(appointment => (
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
    this.modalService.open(InspectAppointmentComponent, { size: 'xl' })
      .componentInstance.appointment = appointment;
  }
}