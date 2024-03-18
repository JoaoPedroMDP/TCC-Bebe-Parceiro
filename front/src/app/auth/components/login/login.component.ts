import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { SwalFacade } from 'src/app/shared';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  isLoading!: boolean;

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    this.isLoading = false;
  }

  /**
   * @Description A Fazer
   */
  login () {
    this.isLoading = true;
    this.authService.login(this.form.value).subscribe({
      next: (response) => {
        /// codigo do retorno de login
      },
      error: () => {
        SwalFacade.error("Erro ao fazer login", "Problema no servidor");
      },
      complete:() => {
        this.isLoading = false;
      }
    });
  }

}
