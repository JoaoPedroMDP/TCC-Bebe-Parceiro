import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { AuthService } from 'src/app/auth';
import { City, Country, State, SwalFacade, } from 'src/app/shared';
import { Group } from 'src/app/shared/models/';
import { VolunteerPOST } from 'src/app/shared/models/volunteer/volunteer.model';
import { GroupService } from 'src/app/volunteer/services/group.service';
import { VolunteerService } from 'src/app/volunteer/services/volunteer.service';


@Component({
  selector: 'app-create-volunteer',
  templateUrl: './create-volunteer.component.html',
  styleUrls: ['./create-volunteer.component.css']
})
export class CreateVolunteerComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  volunteer!: VolunteerPOST;

  countrySelected!: number | undefined;
  stateSelected!: number | undefined;
  countries!: Country[];
  states!: State[];
  cities!: City[];

  selectedGroups: Group[] = [];
  groups: Group[] = [];
  selectedGroupId: Number | undefined;

  constructor(public activeModal: NgbActiveModal, private authService: AuthService,
    private volunteerService: VolunteerService, private groupService: GroupService) { }

  ngOnInit(): void {
    this.volunteer = new VolunteerPOST(); // Inicializa um objeto para podermos usar no form
    // Inicializa um array vazio de grupos para poder adicionar e remover novas funções
    this.volunteer.group_ids = [];
    this.listGroups();
    this.listCountries();
  }

  /**
   * @description Cria uma voluntária nova no sistema através do método createVolunteer() do service
   */
  save() {
    // Se as senhas forem iguais então cria o objeto
    if (this.volunteer.password == this.form.value.password_confirm) {
      this.volunteerService.createVolunteer(this.volunteer).subscribe({
        next: () => SwalFacade.success("Voluntária criada com sucesso", `Voluntaria: ${this.volunteer.name}`),
        error: (e) => SwalFacade.error("Erro ao salvar!", e),
        complete: () => this.activeModal.close()
      });
    } else {
      SwalFacade.alert("Não foi possível salvar!", "A senhas devem ser iguais!")
    }
  }

  /**
   * @description Adiciona um grupo/função novo para a voluntária, após isso mostra
   * ele visualmente no HTMl como escolhido e remove do atributo groups para não ser
   * adicionado novamente
   */
  addGroup() {
    // Verifica se o id escolhido existe no array de funcoes/grupos
    const group = this.groups.find(g => g.id === Number(this.selectedGroupId));

    if (group) {
      // Se existir primeiro adiciona aos selecionados para visualizar no HTML
      this.selectedGroups.push(group);
      // então remove ele do array de funcoes/grupos para nao ser adicionado novamente
      this.groups = this.groups.filter(g => g.id !== group.id);
      // Adiciona ele no array do objeto da voluntaria
      if (group.id && this.volunteer.group_ids) {
        this.volunteer.group_ids?.push(group.id);
      }
      // E por fim reseta a model para poder escolher outra funcao
      this.selectedGroupId = undefined;
    }
  }

  /**
   * @description Confirma com o usuário se ele quer remover um grupo da voluntária, caso aceito
   * então remove o objeto da voluntária e adiciona ele no <select> para funcionar de forma dinâmica 
   * @param group O grupo/função a ser removido
   */
  removeGroup(group: Group) {
    // Confirma com o usuário se ele deseja excluir mesmo a função da voluntária
    SwalFacade.delete("Remover a função da voluntária?", "Remover")
      .then((result) => {
        if (result.isConfirmed) {
          // Adiciona ao array dos grupos no Select
          this.groups.push(group);
          // Remove dos grupos da voluntaria
          this.volunteer.group_ids?.filter(id => id !== Number(group.id));
          // Remove do selectedGroups (O array que mostra os grupos escolhidos)
          this.selectedGroups = this.selectedGroups.filter(g => g.id !== group.id);
          // Ordena por nome crescente
          this.groups.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''))
        }
      })
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
