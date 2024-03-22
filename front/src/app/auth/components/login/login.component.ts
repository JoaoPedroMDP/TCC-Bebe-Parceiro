import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { SwalFacade, User, UserToken } from 'src/app/shared';
import { Router } from '@angular/router';

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

  constructor(private authService: AuthService, private router: Router) { }

  ngOnInit(): void {
    this.isLoading = false;
    this.showPassword = false;
  }

  /**
   * @Description Verifica os campos de usuário e senha e faz a chamada no
   * Service para fazer o login, caso bem-sucedido, cria um cookie através
   * do service e o encaminha para sua devida rota
   */
  login() {
    this.isLoading = true; // Flag para carregamento do ícone
    
    this.authService.login(this.form.value).subscribe({
      next: (response) => {
        SwalFacade.success("Login realizado com sucesso",`Bem vindo(a) ${response.user.name}`).then(() => {
          // Atribui os dados do response para um objeto token e o salva no AuthService
          this.token = response;
          this.authService.setUser(this.token);
          console.log(this.token);

          if (this.token.user?.role == "volunteer") {
            // navega pro componente homepage voluntaria
            this.router.navigate(['/admin']);
          } else if(this.token.user?.role == "admin") {
            // navega pro componente homepage admin
            this.router.navigate(['/admin']);
          } else {
            // navega pro componente homepage beneficiada
            this.router.navigate(['/beneficiada']);
          }
        })
      },
      error: (e) => {
        let errorMessage
        switch (e.message) {
          case '400':
            errorMessage = 'Telefone ou senha incorretos!';
            break;
          case '403':
            errorMessage = 'Acesso Proibido! Conta já logada.';
            break;
          default:
            errorMessage = 'Erro inesperado. Tente novamente mais tarde.';
        }
        SwalFacade.error("Erro ao fazer login", errorMessage);
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
