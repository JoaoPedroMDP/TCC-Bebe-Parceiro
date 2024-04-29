import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { Beneficiary, SwalFacade, UserToken } from 'src/app/shared';
import { BeneficiaryService } from '../../services/beneficiary.service';
import { RemoveInformationComponent } from '../remove-information/remove-information.component';

@Component({
  selector: 'app-view-information',
  templateUrl: './view-information.component.html',
  styleUrls: ['./view-information.component.css']
})
export class ViewInformationComponent implements OnInit {

  beneficiary!: Beneficiary;
  subscription: Subscription | undefined;

  constructor(
    private beneficiaryService: BeneficiaryService,
    private authService: AuthService,
    private router: Router,
    private modalService: NgbModal
  ) { }

  ngOnInit(): void {
    this.beneficiary = new Beneficiary(); // só pra não dar erro de undefined
    // Lógica diferente do inspect pela beneficiada, não uso nada do router
    // Só pego o user dos cookies e depois chamo o findBeneficiary() para
    // encontrar a beneficiada
    let user: UserToken = this.authService.getUser();
    this.beneficiaryService.findBeneficiary(user.person_id!).subscribe({
      next: (response) => this.beneficiary = response,
      error: (e) => {
        SwalFacade.error("Ocorreu um erro!", e)
        this.router.navigate(['/'])
      },
    });
  }

  /**
   * @description Abre um modal para excluir a beneficiada
   */
  deleteBeneficiary() {
    this.modalService.open(
      RemoveInformationComponent, { size: 'xl' }
    ).componentInstance.beneficiary = this.beneficiary!;
  }
}
