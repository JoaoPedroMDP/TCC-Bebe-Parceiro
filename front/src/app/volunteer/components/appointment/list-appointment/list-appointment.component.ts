import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Appointment } from 'src/app/shared/models/appointment/appointment.model';
import { AppointmentService } from 'src/app/volunteer/services/appointment.service';

@Component({
  selector: 'app-list-appointment',
  templateUrl: './list-appointment.component.html',
  styleUrls: ['./list-appointment.component.css']
})
export class ListAppointmentComponent implements OnInit {

  appointments!: Appointment[];
  // filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private router: Router, private appointmentService: AppointmentService) { }

  ngOnInit(): void {
    this.listAppointments() // Lista inicialmente os profissionais pendentes
    this.subscription = this.appointmentService.refreshPage$.subscribe(() => {
      this.listAppointments(); // Lista os beneficiados novamente para refletir as atualizações.
    })
  }

  ngOnDestroy(): void {
    // Cancela a subscrição para evitar vazamentos de memória.
    this.subscription?.unsubscribe();
  }

  listAppointments() {
    this.appointmentService.listAppointments().subscribe({
      next: (response) => {
        this.appointments = response
        // Ordena por nome crescente
        this.appointments.sort((a, b) => (a.beneficiary?.user?.name ?? '').localeCompare(b.beneficiary?.user?.name ?? ''))
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.isLoading = false
    })
  }


  /**
 * @description Abre o modal de inspeção
 * @param professional objeto do profissional para ir como variavel no componente
 */
  inspectAppointment(professional: Appointment) {
    // let modalRef = this.modalService.open(InspectProfessionalComponent, { size: 'xl' });
    // modalRef.componentInstance.professional = professional;    // Passando o profissional
    // modalRef.componentInstance.isProfessionalApproved = true; // Passando o modo de edição
  }

  newAppointment(){}
}
