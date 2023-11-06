import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-auto-cadastro',
  templateUrl: './auto-cadastro.component.html',
  styleUrls: ['./auto-cadastro.component.css']
})
export class AutoCadastroComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  EstadoCivil!: string[];

  constructor() { }

  ngOnInit(): void {
    this.EstadoCivil = ['Solteira','Casada','Separada','Divorciada','Viúva'];
  }

}
