import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Professional } from 'src/app/shared/models/professional';
import { ProfessionalService } from 'src/app/volunteer/services/professional.service';
import { InspectProfessionalComponent } from '../index';

@Component({
  selector: 'app-list-professional',
  templateUrl: './list-professional.component.html',
  styleUrls: ['./list-professional.component.css']
})
export class ListProfessionalComponent implements OnInit, OnDestroy {

  professionals!: Professional[];
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private router: Router, private professionalService: ProfessionalService) { }

  ngOnInit(): void {
    this.listProfessionals(false)
  }
  
  ngOnDestroy(): void {
    // Cancela a subscrição para evitar vazamentos de memória.
    this.subscription?.unsubscribe();
  }

  listProfessionals(isFiltering: boolean){
    this.isLoading = true; // Flag de carregamento
    this.professionalService.listProfessionals().subscribe({
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
        this.listProfessionals(true)
      } else {
        // se não tiver então a gente filtra tudo
        this.listProfessionals(false);
      }
    }
  }

  inspectProfessional(professional: Professional){
    this.modalService.open(
      InspectProfessionalComponent, { size: 'xl' }
    ).componentInstance.professional = professional;
  }
  editProfessional(professional: Professional) {}
  deleteProfessional(professional: Professional) {}
  newProfessional(){}
}
