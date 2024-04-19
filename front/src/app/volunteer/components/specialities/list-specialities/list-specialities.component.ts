import { Component, OnDestroy, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Speciality } from 'src/app/shared/models/professional';
import { SpecialityService } from 'src/app/volunteer/services/speciality.service';

@Component({
  selector: 'app-list-specialities',
  templateUrl: './list-specialities.component.html',
  styleUrls: ['./list-specialities.component.css']
})
export class ListSpecialitiesComponent implements OnInit, OnDestroy {

  specialities!: Speciality[];
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private specialityService: SpecialityService, private modalService: NgbModal) { }

  ngOnInit(): void {
    this.listSpecialities(false); // Inicialmente lista as especialidades.
    // Se inscreve no Observable de atualização. Quando um novo valor é emitido, chama a listagem novamente.
    this.subscription = this.specialityService.refreshPage$.subscribe(() => {
      this.listSpecialities(false); // Lista os beneficiados novamente para refletir as atualizações.
    })
  }

  ngOnDestroy(): void {
    this.subscription?.unsubscribe(); // Cancela a subscrição para evitar vazamentos de memória.
  }

  listSpecialities(isFiltering: boolean){
    this.isLoading = true; // Flag de carregamento
    this.specialityService.listSpecialities().subscribe({
      next: (response) => {
        this.specialities = response
        // Ordena por nome crescente
        this.specialities.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''))
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => { 
        if (isFiltering) {
          this.specialities = this.specialities.filter(
            (speciality: Speciality) => {
              // Asegura que name é uma string antes de chamar métodos de string
              return speciality.name ? speciality.name.toLowerCase().includes(this.filter.toLowerCase()) : false;
            }
          );
        }
        this.isLoading = false;
      }
    })
  }

  
  deleteSpeciality(speciality: Speciality){

  }
  

  editSpeciality(speciality: Speciality){

  }

  /**
   * @description Verifica se o usuário está filtrando dados e chama os métodos
   * @param event Um evento do input
   */
  filterSpeciality(event: Event) {
    if (event != undefined) {
      this.specialities = []; // Esvazia o array

      // A ideia tem que ser se tiver string então filtrar 
      if (this.filter != '') {
        this.listSpecialities(true)
      } else {
        // se não tiver então a gente filtra tudo
        this.listSpecialities(false);
      }
    }
  }

  newSpeciality(){

  }
}
