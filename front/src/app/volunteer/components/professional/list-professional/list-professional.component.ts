import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Professional } from 'src/app/shared/models/professional';
import { ProfessionalService } from 'src/app/volunteer/services/professional.service';

@Component({
  selector: 'app-list-professional',
  templateUrl: './list-professional.component.html',
  styleUrls: ['./list-professional.component.css']
})
export class ListProfessionalComponent implements OnInit {

  professionals!: Professional[];
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private router: Router, private professionalService: ProfessionalService) { }

  ngOnInit(): void {
    this.listProfessionals(false)
  }

  listProfessionals(isFiltering: boolean){
    this.isLoading = true; // Flag de carregamento

    if (isFiltering) {
      this.professionalService.listProfessionals()
        .subscribe(response => {
          this.professionals = response.filter(
            // Compara filtro com o array tudo em lowercase
            (p: { name: string; }) => p.name.toLowerCase().includes(this.filter.toLowerCase())
          );
          // Ordena por nome crescente
          this.professionals.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''))
          this.isLoading = false;
        });
    } else {
      this.professionalService.listProfessionals().subscribe({
        next: (response) => {
          this.professionals = response
          this.isLoading = false;
          console.log(this.professionals);
          
        },
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      })
    }    
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

  inspectProfessional(professional: Professional){}
  editProfessional(professional: Professional) {}
  deleteProfessional(professional: Professional) {}
  newProfessional(){}
}
