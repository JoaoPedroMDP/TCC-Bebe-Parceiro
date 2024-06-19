import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Appointment } from 'src/app/shared';


@Component({
  selector: 'app-inspect-appointment',
  templateUrl: './inspect-appointment.component.html',
  styleUrls: ['./inspect-appointment.component.css']
})
export class InspectAppointmentComponent implements OnInit {

  @Input() appointment!: Appointment;
 
  constructor(public activeModal: NgbActiveModal) { }

  ngOnInit(): void {}

}
