import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { BeneficiaryService } from 'src/app/beneficiary/services/beneficiary.service';
import { Appointment, Professional, SwalFacade, } from 'src/app/shared';


@Component({
  selector: 'app-inspect-appointment',
  templateUrl: './inspect-appointment.component.html',
  styleUrls: ['./inspect-appointment.component.css']
})
export class InspectAppointmentComponent implements OnInit {

  appointment!: Appointment;
  @Input() professional!: Professional;
  @ViewChild('form') form!: NgForm;
 
 

  constructor(public activeModal: NgbActiveModal, public modalService: NgbModal,
    private router: Router,
    private route: ActivatedRoute,
    private beneficiaryService: BeneficiaryService) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const appointmentId = Number(params.get('idAtendimento'));
      if (appointmentId) {
        this.beneficiaryService.findAppointment(appointmentId).subscribe({
          next: (response) => this.appointment = response,
          error: (e) => {
            SwalFacade.error("Ocorreu um erro! Redirecionando para a listagem", e)
            this.router.navigate(['/beneficiada/atendimentos'])
          }
        });
      }
    });
  }

}
