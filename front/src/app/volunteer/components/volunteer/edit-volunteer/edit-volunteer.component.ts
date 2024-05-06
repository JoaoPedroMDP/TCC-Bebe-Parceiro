import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { AuthService } from 'src/app/auth';
import { City, Country, State, SwalFacade, } from 'src/app/shared';
import { Group } from 'src/app/shared/models/';
import { VolunteerPOST } from 'src/app/shared/models/volunteer/volunteer.model';
import { GroupService } from 'src/app/volunteer/services/group.service';
import { VolunteerService } from 'src/app/volunteer/services/volunteer.service';


@Component({
  selector: 'app-edit-volunteer',
  templateUrl: './edit-volunteer.component.html',
  styleUrls: ['./edit-volunteer.component.css']
})
export class EditVolunteerComponent implements OnInit {
  
  @ViewChild('form') form!: NgForm;
  @Input() volunteer!: VolunteerPOST;
  @Input() editMode!: boolean;
  @Input() countrySelected!: number | undefined;
  @Input() stateSelected!: number | undefined;

  countries!: Country[];
  states!: State[];
  cities!: City[];
  selectedGroups: Group[] = [];
  groups: Group[] = [];
  selectedGroupId: Number | undefined;

  constructor(public activeModal: NgbActiveModal,
    private authService: AuthService,
    private volunteerService: VolunteerService,
    private groupService: GroupService
  ) { }

  ngOnInit(): void {
    // Salva duas variáveis locais de estado e cidade
    // Isso é feito pois quando for chamado o método de listar países
    // ele vai limpar os estados e cidades
    let auxState = this.stateSelected;
    let auxCity = this.volunteer.city_id;

    if (this.editMode) {
      this.getDataFromEditing();
    } else {
      this.listGroups();
    }
    this.listCountries();
    this.listStates();
    this.stateSelected = auxState; // Recupera a variável local
    this.listCities();
    this.volunteer.city_id = auxCity; // Recupera a variável local  
  }

  getDataFromEditing() {
    // Eu não sei o porquê, mas quando é para editar o método listGroups() não funciona
    // Então fazemos ele aqui dentro desse outro método
    this.groupService.listGroups().subscribe({
      next: (data: Group[]) => {
        if (data != null) {
          this.groups = data;
          // Ordena por nome crescente
          this.groups.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''))
        }
      },
      error: (e) => SwalFacade.error('Erro ao listar os dados de funções', e),
      complete: () => {
        if (Array.isArray(this.volunteer.group_ids)) {
          // Remove o grupo com ID 15 da lista de grupos disponíveis (this.groups)
          this.volunteer.group_ids = this.volunteer.group_ids.filter(group => group !== 15); // EXCLUIR DEPOIS, role volunteer nao era para estar vindo

          this.volunteer.group_ids.forEach(groupId => {
            const group = this.groups.find(g => g.id === Number(groupId));
            if (group) {
              this.selectedGroups.push(group);
              this.groups = this.groups.filter(g => g.id !== group.id);
            }
          });
        }
      },
    })

  }

  addGroup() {
    // Verifica se o id existe
    if (this.selectedGroupId) {
      // Verifica se o id escolhido existe no array de funcoes/grupos
      const group = this.groups.find(g => g.id === Number(this.selectedGroupId));

      if (group) {
        // Se existir primeiro adicione aos selecionados
        this.selectedGroups.push(group);
        // então remova ele do array de funcoes/grupos para nao ser adicionado novamente
        this.groups = this.groups.filter(g => g.id !== group.id);
        // this.volunteer.group_ids?.push(group?.id)

        if (!Array.isArray(this.volunteer.group_ids)) {
          this.volunteer.group_ids = [];
        }
        if (group.id && this.volunteer.group_ids) {
          this.volunteer.group_ids?.push(group.id);
        }
        // E por fim reseta a model para poder escolher outra funcao
        this.selectedGroupId = undefined;
      }
    }
  }

  removeGroup(group: Group) {
    SwalFacade.delete("Remover a função da voluntária?", "Remover")
      .then((result) => {
        if (result.isConfirmed) {
          this.groups.push(group);
          this.volunteer.group_ids?.filter(id => id !== Number(group.id));
          this.selectedGroups = this.selectedGroups.filter(g => g.id !== group.id);
          // Ordena por nome crescente
          this.groups.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''))
          if (this.editMode && Array.isArray(this.volunteer.group_ids)) {
            this.volunteer.group_ids = this.volunteer.group_ids.filter(id => id !== group.id);
          }
        }
      })
  }

  save() {
    if (!this.volunteer.password || this.volunteer.password == this.form.value.password_confirm) {
      // if (this.editMode) {
      //   this.volunteerService.editVolunteer(this.volunteer.id!, this.volunteer).subscribe({
      //     next: () => SwalFacade.success("Sucesso!", `${this.volunteer.name} foi atualizado com sucesso!`),
      //     error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      //   });
      // } else {
      //   this.volunteerService.createVolunteer(this.volunteer).subscribe({
      //     next: () => SwalFacade.success("Voluntária criada com sucesso", `Voluntaria: ${this.volunteer.name}`),
      //     error: (e) => SwalFacade.error("Erro ao salvar!", e)
      //   });
      // }
      console.log('TRUE');
      
    } else {
      console.log('FALSE');
      SwalFacade.alert("Não foi possível salvar!","A senhas devem ser iguais!")
    }
    console.log(this.volunteer);
    this.activeModal.close();
  }



  /**
   * @description Obtém  a lista de funções.
   */
  listGroups() {
    this.groupService.listGroups().subscribe({
      next: (data: Group[]) => {
        if (data == null) {
          this.groups = [];
        } else {
          this.groups = data;
          // Ordena por nome crescente
          this.groups.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''))
        }
      },
      error: (e) => SwalFacade.error('Erro ao listar os dados de funções', e)
    })
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
    this.volunteer.city_id = undefined;

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
  close() {
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
