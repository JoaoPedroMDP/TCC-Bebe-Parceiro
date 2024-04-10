import { Component, OnDestroy, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Benefited, SwalFacade } from 'src/app/shared';
import { VolunteerService } from 'src/app/volunteer/services/volunteer.service';
import { DeleteBeneficiaryComponent } from '../delete-beneficiary/delete-beneficiary.component';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-list-beneficiary',
  templateUrl: './list-beneficiary.component.html',
  styleUrls: ['./list-beneficiary.component.css']
})
export class ListBeneficiaryComponent implements OnInit, OnDestroy {

  beneficiaries!: Benefited[];
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private volunteerService: VolunteerService, private modalService: NgbModal, private router: Router) { }

  ngOnInit(): void {
    this.listBenefited(false); // Inicialmente lista os beneficiados.
    // Se inscreve no Observable de atualização. Quando um novo valor é emitido, chama a listagem novamente.
    this.subscription = this.volunteerService.refreshPage$.subscribe(() => {
      this.listBenefited(false); // Lista os beneficiados novamente para refletir as atualizações.
    })
  }

  ngOnDestroy(): void {
    // Cancela a subscrição para evitar vazamentos de memória.
    this.subscription?.unsubscribe();
  }

  /**
   * @description Lista todas as beneficiadas no componente
   * @param isFiltering boolean que indica se a listagem será filtrada ou não
   */
  listBenefited(isFiltering: boolean) {
    this.isLoading = true; // Flag de carregamento

    if (isFiltering) {
      this.volunteerService.listBenefited()
        .subscribe(response => {
          this.beneficiaries = response.filter(
            // Compara filtro com o array tudo em lowercase
            (ben: { name: string; }) => ben.name.toLowerCase().includes(this.filter.toLowerCase())
          );
          // Ordena por nome crescente
          this.beneficiaries.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''))
          this.isLoading = false;
        });
    } else {
      this.volunteerService.listBenefited().subscribe({
        next: (response) => {
          this.beneficiaries = response
          this.isLoading = false;
        },
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      })
    }
  }

  /**
   * @description Navega para a rota de atendimentos da beneficiada
   * @param benefited objeto da beneficiada para ir como parâmetro na rota
   */
  appointmentsForBenefited(benefited: Benefited) {
    SwalFacade.alert("Rota ainda não desenvolvida", "Não foi possível ver os atendimentos da beneficiada")
  }

  /**
   * @description Navega para a rota de edição da beneficiada
   * @param benefited objeto da beneficiada para ir como parâmetro na rota
   */
  deleteBenefited(benefited: Benefited) {
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

  /**
   * @description Verifica se o usuário está filtrando dados e chama os métodos
   * @param event Um evento do input
   */
  filterBenefited(event: Event) {
    if (event != undefined) {
      this.beneficiaries = []; // Esvazia o array

      // A ideia tem que ser se tiver string então filtrar 
      if (this.filter != '') {
        this.listBenefited(true)
      } else {
        // se não tiver então a gente filtra tudo
        this.listBenefited(false);
      }
    }
  }

  /**
   * @description Navega para a rota de inspeção e verificar os dados da beneficiada
   * @param benefited objeto da beneficiada para ir como parâmetro na rota
   */
  inspectBenefited(benefited: Benefited) {
    this.router.navigate(['/voluntaria/beneficiadas/inspecionar', benefited.id])
  }
}