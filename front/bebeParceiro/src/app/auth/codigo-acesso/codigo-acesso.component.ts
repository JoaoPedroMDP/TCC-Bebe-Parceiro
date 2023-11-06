import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AuthService } from '../index';
import { Router } from '@angular/router';

@Component({
  selector: 'app-codigo-acesso',
  templateUrl: './codigo-acesso.component.html',
  styleUrls: ['./codigo-acesso.component.css']
})
export class CodigoAcessoComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  constructor(private authService: AuthService, private router: Router) { }

  ngOnInit(): void {
  }

  /**
   * @description 
   * Valida o código de acesso para redirecionar ao formulário de cadastro
   * 
   */
  cadastrar() {
    console.log(this.form.value.codigo);
    
    this.router.navigate(['autocadastro/dados'])
    // this.authService.validarCodigo(this.form.value.codigo).subscribe({
    //   next: (sucesso) => { 
    //     console.log(sucesso) 
    //   },
    //   error: (e) => console.log(e)
    // })
  }

}
