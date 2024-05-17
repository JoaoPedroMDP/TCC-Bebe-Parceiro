import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { AuthService } from 'src/app/auth';
import { SwalFacade, UserToken } from 'src/app/shared';
import { RequestSwapComponent } from '../request-swap/request-swap.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  user!: UserToken;

  constructor(private authService: AuthService, private router: Router, private modalService: NgbModal) { }

  ngOnInit(): void {
    this.user = this.authService.getUser();
  }

  /**
   * @Description Realiza o logout do usuário e retorna a página de login
   */
  logout() {
    this.authService.logout().subscribe({
      next: () => SwalFacade.success("Usuário desconectado", "Redirecionando ao login"),
      error: (e) => SwalFacade.error("Ocorreu um erro", e),
      complete: () => this.router.navigate(['/login'])
    });
  }

  /**
   * @Description Abre um modal para pedir uma troca
   */
  openSwapModal() {
    this.modalService.open(RequestSwapComponent, { size: 'xl' });
  }
}
