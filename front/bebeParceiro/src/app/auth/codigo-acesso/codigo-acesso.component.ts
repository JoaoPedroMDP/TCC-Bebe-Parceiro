import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AuthService } from '../index';
import { Router } from '@angular/router';
import { SwalFacade } from 'src/app/shared/swal-facade';

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
  validateAccessCode() {
    this.authService.sendCode(this.form.value.codigo).subscribe({
      next: (aaa) => {
        console.log('dados=>' + aaa)

        if (aaa != '') {
          SwalFacade.success('Código Válido!')

          this.router.navigate(['autocadastro/dados'])

        } else {
          SwalFacade.error('Código Inválido', 'Entre em contato com a voluntária')
        }
      },
      error: (e) => console.log(e)
    })
  }

}
