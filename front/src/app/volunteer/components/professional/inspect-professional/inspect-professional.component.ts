import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Professional } from 'src/app/shared/models/professional';
import { DeleteProfessionalComponent } from '../delete-professional/delete-professional.component';

@Component({
  selector: 'app-inspect-professional',
  templateUrl: './inspect-professional.component.html',
  styleUrls: ['./inspect-professional.component.css']
})
export class InspectProfessionalComponent implements OnInit {

  @Input() professional!: Professional;

  constructor(public activeModal: NgbActiveModal, public modalService: NgbModal) { }

  ngOnInit(): void {
    console.log(this.professional);
    
  }

  editProfessional(professional: Professional){
    // this.modalService.open(
    //   CreateEditProfessionalComponent, { size: 'xl' }
    // ).componentInstance.professional = professional;
  }

  deleteProfessional(professional: Professional){
    this.modalService.open(
      DeleteProfessionalComponent, { size: 'xl' }
    ).componentInstance.professional = professional;
  }
}
