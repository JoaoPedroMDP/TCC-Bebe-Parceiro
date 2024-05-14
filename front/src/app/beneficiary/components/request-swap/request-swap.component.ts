import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { BeneficiaryService } from '../../services/beneficiary.service';

@Component({
  selector: 'app-request-swap',
  templateUrl: './request-swap.component.html',
  styleUrls: ['./request-swap.component.css']
})
export class RequestSwapComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  showSuccess!: boolean;
  // accessCodes!: AccessCode[];

  constructor(public activeModal: NgbActiveModal, private beneficiaryService: BeneficiaryService) { }

  ngOnInit(): void {
  }

  requestTrade(){
    this.showSuccess = !this.showSuccess
  }
}
