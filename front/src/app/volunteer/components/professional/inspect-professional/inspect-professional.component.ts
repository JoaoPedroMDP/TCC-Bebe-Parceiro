import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Professional } from 'src/app/shared/models/professional';

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

  }

  deleteProfessional(professional: Professional){

  }
}
