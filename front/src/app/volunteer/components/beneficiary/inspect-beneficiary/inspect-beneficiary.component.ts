import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Benefited, SwalFacade } from 'src/app/shared';
import { VolunteerService } from 'src/app/volunteer/services/volunteer.service';
import { DeleteBeneficiaryComponent } from '../delete-beneficiary/delete-beneficiary.component';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-inspect-beneficiary',
  templateUrl: './inspect-beneficiary.component.html',
  styleUrls: ['./inspect-beneficiary.component.css']
})
export class InspectBeneficiaryComponent implements OnInit {

  benefited!: Benefited;
  country!: string;
  state!: string;
  city!: string;
  maritalStatus!: string;


  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private volunteerService: VolunteerService,
    private modalService: NgbModal
  ) { }

  ngOnInit(): void {
    // Inicializa um objeto vazio para evitar erros de undefined
    this.benefited = new Benefited();
    // Recupera o objeto da beneficiada através do ID presente na rota
    // Ou seja na url /beneficiadas/inspecionar/9 será recuperado o ID 9 
    // e irá buscar a beneficiada com esse ID e  mostrar os dados dela
    this.route.paramMap.subscribe(params => {
      const benefitedId = Number(params.get('idBeneficiada'));
      if (benefitedId) {
        this.volunteerService.findBenefited(benefitedId).subscribe({
          next: (response) => {
            this.benefited = response
            this.getAddress();
            this.getMaritalStatus();
          },
          error: (e) => {
            SwalFacade.error("Ocorreu um erro! Redirecionando para a listagem", e)
            this.router.navigate(['/voluntaria/beneficiadas'])
          },
        });
      }
    });
  }

  /**
   * @description Procura qual é o endereço da beneficiada através do id
   */
  getAddress() {
    this.volunteerService.findCity(this.benefited.city_id!).subscribe({
      next: (response) => {
        this.city = response.name
        this.state = response.state.name
        this.country = response.state.country.name
      },
      error: (e) => { SwalFacade.error("Ocorreu um erro!", e) },
    })
  }

  /**
   * @description Procura qual é o estado civil da beneficiada através do id
   */
  getMaritalStatus() {
    this.volunteerService.findMaritalStatus(this.benefited.marital_status_id!).subscribe({
      next: (response) => this.maritalStatus = response.name,
      error: (e) => SwalFacade.error("Ocorreu um erro!", e)
    })
  }

  /**
   * @description Navega para a rota de edição da beneficiada
   * @param benefited objeto da beneficiada para ir como parâmetro na rota
   */
  deleteBenefited(benefited: Benefited) {
    this.router.navigate(['/voluntaria/beneficiadas']);
    this.modalService.open(
      DeleteBeneficiaryComponent, { size: 'xl' }
    ).componentInstance.benefited = benefited;
  }

  /**
   * @description Navega para a rota de edição da beneficiada
   * @param benefited objeto da beneficiada para ir como parâmetro na rota
   */
  editBenefited(benefited: Benefited) {
    this.router.navigate(['/voluntaria/beneficiadas/editar', benefited.id])
  }
}
