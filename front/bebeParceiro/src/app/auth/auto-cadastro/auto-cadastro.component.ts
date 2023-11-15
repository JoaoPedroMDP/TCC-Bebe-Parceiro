import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-auto-cadastro',
  templateUrl: './auto-cadastro.component.html',
  styleUrls: ['./auto-cadastro.component.css']
})
export class AutoCadastroComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  EstadoCivil!: string[];

  constructor() { }
  programasSociais: string[] = [];

  paises!: string[];
  estados!: string[];
  cidades!: string[];

  constructor(private router: Router) { }

  ngOnInit(): void {
    this.EstadoCivil = ['Solteira','Casada','Separada','Divorciada','Viúva'];
    this.estadoCivilSelecionado = null;
    this.invalidezSelecionada = false;
    this.programasSociais = ['CRAS', 'Minha Casa Minha Vida', 'Cadastro de Emprego','Cartão Alimentação','Leite das Crianças','Aposentadoria','Bolsa Família'];
  }

  cadastrar() {
    // Filtrar propriedades que não são programas sociais
    // const dadosNaoProgramasSociais = Object.keys(this)
    // .filter(key => !this.programasSociais.includes(key))
    // .reduce((obj: any, key: any) => {
    //   // obj[key] = this[key];
    //   return obj;
    // }, {});

    // // Aqui você pode enviar dadosNaoProgramasSociais junto com outros dados no seu POST
    // console.log('Dados para enviar:', dadosNaoProgramasSociais);
    // console.log('Programas Sociais Selecionados:', this.programasSociaisSelecionados);
  
    console.log(this.form.value)
    console.log('Programas Sociais Selecionados:', this.programasSociaisSelecionados);
    // this.router.navigate(['autocadastro/sucesso'])
  }

  listarPaises(){}
  listarEstados(){}
  listarCidades(){}

  toggleProgramaSocial(programaSocial: string) {
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
