import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { Beneficiada, EstadoCivil, SocialProgram, SwalFacade, Children, Country, State, City } from 'src/app/shared';


@Component({
  selector: 'app-auto-cadastro',
  templateUrl: './auto-cadastro.component.html',
  styleUrls: ['./auto-cadastro.component.css']
})
export class AutoCadastroComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  beneficiada!: Beneficiada;
  // children!: Children;

  estadoCivil!: EstadoCivil[];
  programasSociaisSelecionados: SocialProgram[] = [];
  programasSociais: SocialProgram[] = [];
  countrySelected!: number | undefined;
  stateSelected!: number | undefined;

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
    this.beneficiada.socialProgram = this.programasSociaisSelecionados;
    // this.beneficiada.children = ;

    console.log(this.beneficiada);

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

  listStates() {
    this.states = []; // Trocou o país então precisa limpar os estados
    this.cities = []; // Trocou o país então precisa limpar as cidades
    this.stateSelected = undefined;
    console.log(this.stateSelected)
    if (this.countrySelected != null) {
      this.authService.getStates(this.countrySelected).subscribe({
        next: (data: State[]) => {
          console.log(data)
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
      next: (data: SocialProgram[]) => {
        if (data == null) {
          this.programasSociais = [];
        } else {
          this.programasSociais = data;
        }
      },
      error: () => SwalFacade.error('Erro ao listar os dados de Estado Civil')
    })
  }

  toggleProgramaSocial(programaSocial: SocialProgram) {
    const index = this.programasSociaisSelecionados.indexOf(programaSocial);

    if (index !== -1) {
      // Se já está no array, remova
      this.programasSociaisSelecionados.splice(index, 1);
    } else {
      // Se não está no array, adicione
      this.programasSociaisSelecionados.push(programaSocial);
    }
  }

}
