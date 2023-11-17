import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { Beneficiada, EstadoCivil, ProgramaSocial, SwalFacade, FilhoBeneficiada, Country, State, City } from 'src/app/shared';


@Component({
  selector: 'app-auto-cadastro',
  templateUrl: './auto-cadastro.component.html',
  styleUrls: ['./auto-cadastro.component.css']
})
export class AutoCadastroComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  beneficiada!: Beneficiada;
  filho!: FilhoBeneficiada;

  estadoCivil!: EstadoCivil[];
  programasSociaisSelecionados: number[] = [];
  programasSociais: ProgramaSocial[] = [];
  countrySelected!: Country;
  stateSelected!: State;

  countries!: Country[];
  states!: State[];
  cities!: City[];

  constructor(private authService: AuthService, private router: Router) { }

  ngOnInit(): void {
    this.beneficiada = new Beneficiada();
    this.listEstadoCivil();
    this.listprogramasSocial();
    this.listCountries();
  }

  cadastrar() {
    //   // Filtrar propriedades que não são programas sociais
    //   const chavesIncluir = ['dataNascimento', 'email', 'estadoCivil', 'invalidez', 'nome', 'nomeMae', 'numFilhos', 'rendaFamiliar', 'senha', 'senhaConfirma', 'telefone'];

    // // Filtrar propriedades que não são programas sociais
    // const dadosNaoProgramasSociais = Object.keys(this)
    //   .filter(key => chavesIncluir.includes(key))
    //   .reduce((obj: any, key: any) => {
    //     obj[key] = this[key];
    //     return obj;
    //   }, {});
    // delete this.form.value.Aposentado;
    console.log(this.beneficiada);

    //   // Aqui você pode enviar dadosNaoProgramasSociais junto com outros dados no seu POST
    //   console.log('Dados para enviar:', dadosNaoProgramasSociais);
    //   console.log('Programas Sociais Selecionados:', this.programasSociaisSelecionados);

    console.log(this.form.value)
    console.log('Programas Sociais Selecionados:', this.programasSociaisSelecionados);
    // this.router.navigate(['autocadastro/sucesso'])
  }

  listCountries() {
    this.authService.getCountries().subscribe({
      next: (data: Country[]) => {
        if (data == null) {
          this.countries = [];
        } else {
          this.countries = data;
        }
      },
      error: () => SwalFacade.error('Erro ao listar os dados de Paises')
    })
  }

  listStates(country: Country) {
    if (country.id != undefined) {
      this.authService.getStates(country.id).subscribe({
        next: (data: State[]) => {
          if (data == null) {
            this.states = [];
          } else {
            this.states = data;
          }
        },
        error: () => SwalFacade.error('Erro ao listar os dados de Estados')
      })
    }
  }

  listCities(state: State) { 
    if (state.id != undefined) {
      this.authService.getCities(state.id).subscribe({
        next: (data: State[]) => {
          if (data == null) {
            this.cities = [];
          } else {
            this.cities = data;
          }
        },
        error: () => SwalFacade.error('Erro ao listar os dados de Cidades')
      })
    }
  }

  listEstadoCivil() {
    this.authService.getEstadoCivil().subscribe({
      next: (data: EstadoCivil[]) => {
        if (data == null) {
          this.estadoCivil = [];
        } else {
          this.estadoCivil = data;
        }
      },
      error: () => SwalFacade.error('Erro ao listar os dados de Estado Civil')
    })
  }

  listprogramasSocial() {
    this.authService.getProgramasSociais().subscribe({
      next: (data: ProgramaSocial[]) => {
        if (data == null) {
          this.programasSociais = [];
        } else {
          this.programasSociais = data;
        }
      },
      error: () => SwalFacade.error('Erro ao listar os dados de Estado Civil')
    })
  }

  toggleProgramaSocial(programaSocial: ProgramaSocial) {
    const index = this.programasSociaisSelecionados.indexOf(programaSocial.id);

    if (index !== -1) {
      // Se já está no array, remova
      this.programasSociaisSelecionados.splice(index, 1);
    } else {
      // Se não está no array, adicione
      this.programasSociaisSelecionados.push(programaSocial.id);
    }
  }

}
