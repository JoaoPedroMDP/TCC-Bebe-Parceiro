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
import { Groups_id } from 'src/app/shared/models/volunteer';

@Component({
  selector: 'app-create-volunteer',
  templateUrl: './create-volunteer.component.html',
  styleUrls: ['./create-volunteer.component.css']
})
export class CreateVolunteerComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  @Input()volunteer!: VolunteerPOST;

 
  @Input() editMode!: boolean;
  
  countrySelected!: number | undefined;
  stateSelected!: number | undefined;
  countries!: Country[];
  states!: State[];
  cities!: City[];
  selectedGroups: Groups_id[] = [];
  groups_id: Groups_id[]= [];



    constructor(public activeModal: NgbActiveModal,
      private authService: AuthService, 
      private volunteerService: VolunteerService, 
      private groupService: GroupService,
      private router: Router) { }

    ngOnInit(): void {
      this.volunteer = new VolunteerPOST();
      this.listGroups();
      this.listCountries();
    }
    
  


  save() {
    this.volunteer.groups_id = this.selectedGroups;

    if (this.editMode) {
      this.volunteerService.editVolunteer(this.volunteer.id!, this.volunteer).subscribe({
        next: () => SwalFacade.success("Sucesso!", `${this.volunteer.name} foi atualizado com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      });
    } else {
      if (this.volunteer.password != this.form.value.password_confirm) 
       this.volunteerService.createVolunteer(this.volunteer)
        .subscribe({
          next: () => {
            SwalFacade.success("Voluntária criada com sucesso", `Voluntaria: ${this.volunteer.name}`)
            this.router.navigate(['/voluntaria/voluntarias'])
          },
          error: (e) => SwalFacade.error("Erro ao salvar!", e)
        });
    }
    this.activeModal.close();
  }

  /**
  
  /**
   * @description Obtém  a lista de funções.
   */
  listGroups() {
    this.authService.getGroups().subscribe({
      next: (data: Groups_id[]) => {
        if (data == null) {
          this.groups_id = [];
        } else {
          this.groups_id = data;
        }
      },
      error: (e) => SwalFacade.error('Erro ao listar os dados de funções', e)
    })
  }

   /**
   * @description Adiciona ou remove uma função da lista selecionada.
   * @param groups_id a função a ser removido ou adicionado
   */
   toggleGroups(groups_id: Groups_id) {
    const index = this.selectedGroups.indexOf(groups_id);

    if (index !== -1) {
      // Se já está no array, remova
      this.selectedGroups.splice(index, 1);
    } else {
      // Se não está no array, adicione
      this.selectedGroups.push(groups_id);
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
