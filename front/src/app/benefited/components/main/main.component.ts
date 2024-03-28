import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth';
import { SwalFacade, UserToken } from 'src/app/shared';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  user!: UserToken;
  dropdownOpen: boolean = false;

  constructor(private authService: AuthService, private router: Router) { }

  ngOnInit(): void {
    this.user = this.authService.getUser();
  }

  /**
   * @Description Realiza o logout do usuário e retorna a página de login
   */
  logout() {
    this.authService.logout().subscribe({
      next: () => SwalFacade.success("Usuário desconectado", "Redirecionando ao login"),
      error: () => SwalFacade.error("Ocorreu um erro", "Não foi possível fazer o logout"),
      complete: () => this.router.navigate(['/login'])
    });
  }

  toggleDropdown() {
    this.dropdownOpen = !this.dropdownOpen;
  }
}
