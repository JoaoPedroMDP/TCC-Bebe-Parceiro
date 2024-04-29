import { Component, OnDestroy, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Professional, ProfessionalPOST } from 'src/app/shared/models/professional';
import { ProfessionalService } from 'src/app/volunteer/services/professional.service';
import { ApproveRefuseProfessionalComponent } from '../approve-refuse-professional/approve-refuse-professional.component';
import { InspectProfessionalComponent } from '../inspect-professional/inspect-professional.component';

@Component({
  selector: 'app-list-pending-professionals',
  templateUrl: './list-pending-professionals.component.html',
  styleUrls: ['./list-pending-professionals.component.css']
})
export class ListPendingProfessionalsComponent implements OnInit, OnDestroy {

  professionals!: Professional[];
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private professionalService: ProfessionalService) { }

  ngOnInit(): void {
    this.listPendingProfessionals(false) // Lista inicialmente os profissionais pendentes
    this.subscription = this.professionalService.refreshPage$.subscribe(() => {
      this.listPendingProfessionals(false); // Lista os beneficiados novamente para refletir as atualizações.
    })
  }

  ngOnDestroy(): void {
    // Cancela a subscrição para evitar vazamentos de memória.
    this.subscription?.unsubscribe();
  }

  /**
   * @description Lista os profissionais pendentes
   * @param isFiltering boolean que indica se a listagem será filtrada ou não
   */
  listPendingProfessionals(isFiltering: boolean) {
    this.isLoading = true; // Flag de carregamento
    this.professionalService.listPendingProfessionals().subscribe({
      next: (response) => {
        this.professionals = response
        // Ordena por nome crescente
        this.professionals.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''))
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => {
        if (isFiltering) {
          this.professionals = this.professionals.filter(
            (professional: Professional) => {
              // Asegura que name é uma string antes de chamar métodos de string
              return professional.name ? professional.name.toLowerCase().includes(this.filter.toLowerCase()) : false;
            }
          );
        }
        this.isLoading = false;
      }
    })
  }

  /**
   * @description Verifica se o usuário está filtrando dados e chama os métodos
   * @param event Um evento do input
   */
  filterProfessional(event: Event) {
    if (event != undefined) {
      this.professionals = []; // Esvazia o array

      // A ideia tem que ser se tiver string então filtrar 
      if (this.filter != '') {
        this.listPendingProfessionals(true)
      } else {
        // se não tiver então a gente filtra tudo
        this.listPendingProfessionals(false);
      }
    }
  }

  /**
   * @description Abre um componente modal para aprovar um profissional
   * @param professional O objeto do profissional
   */
  approveProfessional(professional: Professional) {
    let modalRef = this.modalService.open(ApproveRefuseProfessionalComponent, { size: 'xl' });
    modalRef.componentInstance.professional = professional;  // Passando o profissional
    modalRef.componentInstance.isApproving = true;        // Passando a flag de aprovação
  }

  /**
   * @description Abre um componente modal para visualizar um profissional
   * @param professional O objeto do profissional
   */
  inspectProfessional(professional: Professional) {
    let modalRef = this.modalService.open(InspectProfessionalComponent, { size: 'xl' });
    modalRef.componentInstance.professional = professional;    // Passando o profissional
    modalRef.componentInstance.isProfessionalApproved = false; // Passando o modo de edição
  }

  /**
   * @description Abre um componente modal para rejeitar um profissional
   * @param professional O objeto do profissional
   */
  refuseProfessional(professional: Professional) {
    let modalRef = this.modalService.open(ApproveRefuseProfessionalComponent, { size: 'xl' });
    modalRef.componentInstance.professional = professional;  // Passando o profissional
    modalRef.componentInstance.isApproving = false;        // Passando a flag de remoção
  }
}
