import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-acess-codes-modal',
  templateUrl: './acess-codes-modal.component.html',
  styleUrls: ['./acess-codes-modal.component.css']
})
export class AcessCodesModalComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  showSuccess = false;


  constructor(public activeModal: NgbActiveModal) { }

  ngOnInit(): void {
  }

  generateCodes() {
    console.log(this.form.value.amount);
    this.showSuccess = true;
  }

}
