import { Component, OnDestroy, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade, Appointment } from 'src/app/shared';
import { BeneficiaryService } from '../../../services/beneficiary.service';
import { InspectAppointmentComponent} from '../inspect-appointment/inspect-appointment.component';
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
    this.isLoading = true; // Flag de carregamento
    this.beneficiaryService.listAppointments().subscribe({
      next: (response) => {
        this.originalAppointments = response; // Armazena os Appointments originais para filtragem
        this.filterAppointment(); // Chama o componente de filtragem inicialmente
      },
      error: (e) => {
        SwalFacade.error("Ocorreu um erro!", e); // Manipula erros
        this.isLoading = false; // Desativa a flag de carregamento em caso de erro
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
        appointment.beneficiary?.user?.name?.toLowerCase().includes(filterLower) ||
        appointment.status?.name?.toLowerCase().includes(filterLower))
      );
    } else {
      this.appointments = [...this.originalAppointments]; // Retorna todos os appointments se não há filtro
    }
  }

  /**
   * @description Abre o modal de inspeção
   * @param appointment objeto da troca para ir como variavel no componente
   */
  inspectAppointment(appointment: Appointment) {
    let isAppointmentApproved = appointment.status?.name == "Pendente" ? false : true;
    let isAppointmentClosed = appointment.status?.name == "Encerrado" || appointment.status?.name == "Cancelado" ? true : false;
    let modalRef = this.modalService.open(InspectAppointmentComponent, { size: 'xl' })
    modalRef.componentInstance.appointment = appointment;
    modalRef.componentInstance.isAppointmentApproved = isAppointmentApproved;
    modalRef.componentInstance.isAppointmentClosed = isAppointmentClosed;
  }



}