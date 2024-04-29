import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Beneficiary, SwalFacade } from 'src/app/shared';
import { VolunteerService } from 'src/app/volunteer/services/volunteer.service';
import { DeleteBeneficiaryComponent } from '../delete-beneficiary/delete-beneficiary.component';

@Component({
  selector: 'app-inspect-beneficiary',
  templateUrl: './inspect-beneficiary.component.html',
  styleUrls: ['./inspect-beneficiary.component.css']
})
export class InspectBeneficiaryComponent implements OnInit {

  beneficiary!: Beneficiary;

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private volunteerService: VolunteerService,
    private modalService: NgbModal
  ) { }

  ngOnInit(): void {
    // Inicializa um objeto vazio para evitar erros de undefined
    this.beneficiary = new Beneficiary();
    // Recupera o objeto da beneficiada através do ID presente na rota
    // Ou seja na url /beneficiadas/inspecionar/9 será recuperado o ID 9 
    // e irá buscar a beneficiada com esse ID e  mostrar os dados dela
    this.route.paramMap.subscribe(params => {
      const beneficiaryId = Number(params.get('idBeneficiada'));
      if (beneficiaryId) {
        this.volunteerService.findBeneficiary(beneficiaryId).subscribe({
          next: (response) => this.beneficiary = response,
          error: (e) => {
            SwalFacade.error("Ocorreu um erro! Redirecionando para a listagem", e)
            this.router.navigate(['/voluntaria/beneficiadas'])
          },
        });
      }
    });
  }

  /**
   * @description Navega para a rota de edição da beneficiada
   * @param beneficiary objeto da beneficiada para ir como parâmetro na rota
   */
  deleteBeneficiary(beneficiary: Beneficiary) {
    this.router.navigate(['/voluntaria/beneficiadas']);
    this.modalService.open(
      DeleteBeneficiaryComponent, { size: 'xl' }
    ).componentInstance.beneficiary = beneficiary;
  }

  /**
   * @description Navega para a rota de edição da beneficiada
   * @param beneficiary objeto da beneficiada para ir como parâmetro na rota
   */
  editBeneficiary(beneficiary: Beneficiary) {
    this.router.navigate(['/voluntaria/beneficiadas/editar', beneficiary.id])
  }
}
