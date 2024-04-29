import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Group} from 'src/app/shared/models/';
import { VolunteerPOST} from 'src/app/shared/models/volunteer/volunteer.model';
import { SwalFacade, City, Country, State,} from 'src/app/shared';
import { VolunteerService } from 'src/app/volunteer/services/volunteer.service';
import { GroupService } from 'src/app/volunteer/services/group.service';
import { NgForm } from '@angular/forms';
import { AuthService } from 'src/app/auth';
import { Router } from '@angular/router';

 
@Component({
  selector: 'app-create-edit-volunteer',
  templateUrl: './create-edit-volunteer.component.html',
  styleUrls: ['./create-edit-volunteer.component.css']
})
export class CreateEditVolunteerComponent implements OnInit {

   @ViewChild('form') form!: NgForm;
  @Input() volunteer!: VolunteerPOST;
  @Input() editMode!: boolean;
  
  countrySelected!: number | undefined;
  stateSelected!: number | undefined;
  countries!: Country[];
  states!: State[];
  cities!: City[];
  selectedGroups: Group[] = [];
  groups!: Group[];




    constructor(public activeModal: NgbActiveModal,
      private authService: AuthService, 
      private volunteerService: VolunteerService, 
      private groupService: GroupService
     ) { }

    ngOnInit(): void {
      this.volunteer = new VolunteerPOST();
      this.listGroups();
      this.listCountries();
    }
    
  


  save() {
    if (this.editMode) {
      this.volunteerService.editVolunteer(this.volunteer.id!, this.volunteer).subscribe({
        next: () => SwalFacade.success("Sucesso!", `${this.volunteer.name} foi atualizado com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      });
    } else {
       this.volunteerService.createVolunteer(this.volunteer).subscribe({
          next: () => SwalFacade.success("Voluntária criada com sucesso", `Voluntaria: ${this.volunteer.name}`),
          error: (e) => SwalFacade.error("Erro ao salvar!", e)
        });
    }
    this.activeModal.close();
  }

 
  /**
   * 
   *   /**
   * @description Obtém  a lista de funções.
   */
  listGroups() {
    this.groupService.listGroups().subscribe({
      next: (data: Group[]) => {
        if (data == null) {
          this.groups = [];
        } else {
          this.groups = data;
        }
      },
      error: (e) => SwalFacade.error('Erro ao listar os dados de funções', e)
    })
  }
  
  // /**
  //  * @description Obtém  a lista de funções.
  //  */
  // listGroups2() {
  //   this.authService.getGroups().subscribe({
  //     next: (data: group_ids[]) => {
  //       if (data == null) {
  //         this.group_ids = [];
  //       } else {
  //         this.group_ids = data;
  //       }
  //     },
  //     error: (e) => SwalFacade.error('Erro ao listar os dados de funções', e)
  //   })
  // }

   /**
   * @description Adiciona ou remove uma função da lista selecionada.
   * @param group_ids a função a ser removido ou adicionado
   */
   toggleGroups(group_ids: Group) {
    const index = this.selectedGroups.indexOf(group_ids);

    if (index !== -1) {
      // Se já está no array, remova
      this.selectedGroups.splice(index, 1);
    } else {
      // Se não está no array, adicione
      this.selectedGroups.push(group_ids);
    }
  }



   /** 
   * @description Obtém e atualiza a lista de países.
   */
   listCountries() {
    this.authService.getCountries().subscribe({
      next: (data: Country[]) => {
        if (data == null) {
          this.countries = [];
        } else {
          this.countries = data;
        }
      },
      error: (e) => SwalFacade.error('Erro ao listar os dados de Paises', e)
    })
  }

  /**
    * @description Limpa as listas de estados e cidades ao trocar o país,
    * obtém a lista de estados correspondente e exibe o estado selecionado.
    */
  listStates() {
    this.states = []; // Trocou o país então precisa limpar os estados
    this.cities = []; // Trocou o país então precisa limpar as cidades
    this.stateSelected = undefined;

    if (this.countrySelected != null) {
      this.authService.getStates(this.countrySelected).subscribe({
        next: (data: State[]) => {
          if (data == null) {
            this.states = [];
          } else {
            this.states = data;
          }
        },
        error: (e) => SwalFacade.error('Erro ao listar os dados de Estados', e)
      })
    }
  }

  /**
   * @description Limpa a lista de cidades ao trocar o estado,
   * e obtém a lista de cidades correspondente se o estado selecionado não for nulo.
   */
  listCities() {
    this.cities = []; // Trocou o estado então precisa limpar as cidades
    if (this.stateSelected != null) {
      this.authService.getCities(this.stateSelected).subscribe({
        next: (data: State[]) => {
          if (data == null) {
            this.cities = [];
          } else {
            this.cities = data;
          }
        },
        error: (e) => SwalFacade.error('Erro ao listar os dados de Cidades', e)
      })
    }
  }

  /**
   * @description Fecha a janela modal e chama o Observable de atualização
   */
  fechar() {
    this.activeModal.close();
    this.volunteerService.refreshPage$.next();
  }

  /**
   * @description Altera o tipo dos inputs de senha para texto
   * @param fieldName Qual é o input selecionado
   */
  showPassword(fieldName: string) {
    const inputElement = document.getElementsByName(fieldName)[0] as HTMLInputElement;

    // Verifica se o elemento foi encontrado
    if (inputElement) {
      // Obtém o tipo atual do input (text ou password)
      const currentType = inputElement.type;
      // Altera o tipo do input
      inputElement.type = currentType === 'password' ? 'text' : 'password';
    }
  }
}