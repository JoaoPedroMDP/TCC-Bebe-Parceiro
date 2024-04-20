import { Component, OnInit } from '@angular/core';
import { Beneficiary, SwalFacade, UserToken } from 'src/app/shared';
import { BeneficiaryService } from '../../services/beneficiary.service';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from 'src/app/auth';

@Component({
  selector: 'app-view-information',
  templateUrl: './view-information.component.html',
  styleUrls: ['./view-information.component.css']
})
export class ViewInformationComponent implements OnInit {

  beneficiary!: Beneficiary;

  constructor(
    private beneficiaryService: BeneficiaryService,
    private authService: AuthService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
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


  editBeneficiary() {

  }

  deleteBeneficiary() {

  }
}
