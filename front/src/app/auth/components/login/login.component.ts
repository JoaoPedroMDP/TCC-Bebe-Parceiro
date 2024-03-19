import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { SwalFacade, User, UserToken } from 'src/app/shared';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  isLoading!: boolean;
  token!: UserToken;
  showPassword!: boolean;

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    this.isLoading = false;
    this.showPassword = false;
  }

  /**
   * @Description A Fazer
   */
  login() {
    this.isLoading = true; // Flag para carregamento do ícone
    
    this.authService.login(this.form.value).subscribe({
      next: (response) => {
        if (response.token != null) { 
          // Caso o token exista, então o login foi feito com sucesso
          SwalFacade.success("Login realizado com sucesso").then(() => {
            // Atribui os dados do response para um objeto token e o salva no AuthService
            this.token = response;
            this.authService.setUser(this.token);

            // if (this.token.role = 'benefited') {
            //   // navega pro componente homepage beneficiada
            // this.router.navigate(['/benefited']);
            // }
            // else {
            //   // navega pro componente homepage admin/voluntaria
            // }
          })
        } else {
          SwalFacade.error("Erro ao fazer login", "Problema no servidor");
        }
      },
      error: () => {
        SwalFacade.error("Erro ao fazer login", "Usuário ou senha incorretos");
        this.isLoading = false; // Flag para carregamento do ícone
      },
      complete: () => {
        this.isLoading = false; // Flag para carregamento do ícone
      }
    });
  }

  /**
   * @description Alterna a visibilidade da senha. Caso o usuário clique no 
   * ícone de ver a senha, então o sistema verifica o tipo do input e faz uma
   * troca para o tipo text ou password
   */
  mostrarSenha() {
    this.showPassword = !this.showPassword;
    let inputType = document.getElementById('password');

    if (this.showPassword) {
      inputType?.setAttribute('type', 'text');
    } else {
      inputType?.setAttribute('type', 'password');
    }
  }

}
