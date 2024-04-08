import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Benefited } from 'src/app/shared';

import { VolunteerService } from 'src/app/volunteer/services/volunteer.service';
import { DeleteBeneficiaryComponent } from '../delete-beneficiary/delete-beneficiary.component';

@Component({
  selector: 'app-list-beneficiary',
  templateUrl: './list-beneficiary.component.html',
  styleUrls: ['./list-beneficiary.component.css']
})
export class ListBeneficiaryComponent implements OnInit {

  beneficiaries!: Benefited[];
  filter!: string;

  constructor(private volunteerService: VolunteerService, private modalService: NgbModal) { }

  ngOnInit(): void {
    this.listBenefited();
  }

  listBenefited() {
    this.volunteerService.listBenefited().subscribe({
      next: (filtro) => (
        // Filtro de data, só traz os dados que estão entre a dataInicio e dataFim
        console.log(filtro),
        this.beneficiaries = filtro
      ),
    })
  }

  inspectBenefited(benefited: Benefited){
    console.log(benefited);
    
  }

  newBenefited() {

  }

  editBenefited(benefited: Benefited) {

  }

  deleteBenefited(benefited: Benefited) {
    this.modalService.open(
      DeleteBeneficiaryComponent, { size: 'xl' }
    ).componentInstance.benefited = benefited;
  }

  filterBenefited(event: Event) {
    console.log(this.filter);
  }

  appointmentsForBenefited(benefited: Benefited) { }
}
