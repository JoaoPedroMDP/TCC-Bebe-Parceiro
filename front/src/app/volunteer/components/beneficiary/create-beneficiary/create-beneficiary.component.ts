import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth';
import { BeneficiaryPOST, Child, City, Country, MaritalStatus, SocialProgram, State, SwalFacade } from 'src/app/shared';
import { VolunteerService } from 'src/app/volunteer/services/volunteer.service';

@Component({
  selector: 'app-create-beneficiary',
  templateUrl: './create-beneficiary.component.html',
  styleUrls: ['./create-beneficiary.component.css']
})
export class CreateBeneficiaryComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  beneficiary!: BeneficiaryPOST;

  children: Child[] = [];
  selectedSocialPrograms: SocialProgram[] = [];
  socialPrograms: SocialProgram[] = [];

  maritalStatus!: MaritalStatus[];
  countrySelected!: number | undefined;
  stateSelected!: number | undefined;
  countries!: Country[];
  states!: State[];
  cities!: City[];

  constructor(private authService: AuthService, private volunteerService: VolunteerService, private router: Router) { }

  ngOnInit(): void {
    this.beneficiary = new BeneficiaryPOST();
    this.beneficiary.children = [];
    this.beneficiary.has_disablement = false;
    this.listMaritalStatus();
    this.listSocialProgram();
    this.listCountries();
    this.addChild();
  }

  /**
   * @description Salva os dados da beneficiada, incluindo programas sociais e filhos,
   * e navega para a página de sucesso do autocadastro.
   */
  save() {
    // Atualiza os dados da beneficiada com as informações selecionadas
    this.beneficiary.social_programs = this.selectedSocialPrograms;
    this.beneficiary.children = this.children;
    // Validação da quantidade de filhos
    if (this.beneficiary.child_count! > 30 || this.beneficiary.child_count! < 1) {
      this.beneficiary.child_count = this.beneficiary.children.length
    }

    // Verificação se as senhas inseridas são iguais
    if (this.beneficiary.password != this.form.value.password_confirm) {
      SwalFacade.error('Erro ao salvar beneficiada!', 'As senhas devem ser iguais!')
    } else {
      this.volunteerService.createBeneficiary(this.beneficiary)
        .subscribe({
          next: () => {
            SwalFacade.success("Beneficiada criada com sucesso", `Beneficiada: ${this.beneficiary.name}`)
            this.router.navigate(['/voluntaria/beneficiadas'])
          },
          error: (e) => SwalFacade.error("Erro ao salvar!", e)
        });
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
   * @description Obtém e atualiza a lista de estados civis.
   */
  listMaritalStatus() {
    this.authService.getMaritalStatuses().subscribe({
      next: (data: MaritalStatus[]) => {
        if (data == null) {
          this.maritalStatus = [];
        } else {
          this.maritalStatus = data;
        }
      },
      error: () => SwalFacade.alert('Erro ao listar os dados de Estado Civil')
    })
  }

  /**
   * @description Obtém e atualiza a lista de programas sociais.
   */
  listSocialProgram() {
    this.authService.getSocialPrograms().subscribe({
      next: (data: SocialProgram[]) => {
        if (data == null) {
          this.socialPrograms = [];
        } else {
          this.socialPrograms = data;
        }
      },
      error: (e) => SwalFacade.error('Erro ao listar os dados de Estado Civil', e)
    })
  }

  /**
   * @description Adiciona ou remove um programa social da lista selecionada.
   * @param socialProgram o programa social a ser removido ou adicionado
   */
  toggleSocialProgram(socialProgram: SocialProgram) {
    const index = this.selectedSocialPrograms.indexOf(socialProgram);

    if (index !== -1) {
      // Se já está no array, remova
      this.selectedSocialPrograms.splice(index, 1);
    } else {
      // Se não está no array, adicione
      this.selectedSocialPrograms.push(socialProgram);
    }
  }

  /** 
   * @description Adiciona um novo filho à lista de filhos.
   */
  addChild() {
    this.children.push(new Child());
  }

  /**
   * @description Exclui um componente de filho do formulario
   * @param index Índice do filho a ser removido 
   */
  deleteChild(index: number) {
    if (this.children.length == 1) {
      SwalFacade.alert('Não foi possível remover', 'A beneficiada deve ter pelo menos 1 filho cadastrado!')
    } else {
      // O filho só é excluído caso o usuário confirme a decisão
      SwalFacade.delete('Deseja mesmo remover o filho?', 'Remover')
        .then((result) => {
          if (result.isConfirmed) {
            this.children.splice(index, 1);
          }
        })
    }
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
