import { Component, OnDestroy, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Speciality } from 'src/app/shared/models/professional';
import { SpecialityService } from 'src/app/volunteer/services/speciality.service';
import { DeleteSpecialityComponent } from '../delete-speciality/delete-speciality.component';
import { CreateEditSpecialityComponent } from '../create-edit-speciality/create-edit-speciality.component';

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

  /**
   * @description Lista todas as especialidades no componente
   * @param isFiltering boolean que indica se a listagem será filtrada ou não
   */
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

  /**
   * @description Abre o modal de exclusão
   * @param speciality objeto da especialidade para ir como parâmetro na rota
   */
  deleteSpeciality(speciality: Speciality){
    this.modalService.open(
      DeleteSpecialityComponent, { size: 'xl' }
    ).componentInstance.speciality = speciality;
  }
  
  /**
   * @description Abre o modal de edição
   * @param speciality objeto da especialidade para ir como parâmetro na rota
   */
  editSpeciality(speciality: Speciality){
    let modalRef = this.modalService.open(CreateEditSpecialityComponent, { size: 'xl' });
    modalRef.componentInstance.speciality = speciality;  // Passando o especialidade
    modalRef.componentInstance.editMode = true;          // Passando o modo de edição
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

  /**
   * @description Abre o modal de criação
   */
  newSpeciality(){
    let modalRef = this.modalService.open(CreateEditSpecialityComponent, { size: 'xl' });
    modalRef.componentInstance.speciality = new Speciality();  // Passando o especialidade
    modalRef.componentInstance.editMode = false;          // Passando o modo de edição
  }
}
