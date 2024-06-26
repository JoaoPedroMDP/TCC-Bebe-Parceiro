import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth';
import { SwalFacade, UserToken } from 'src/app/shared';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { AcessCodesModalComponent } from '../acess-codes-modal/acess-codes-modal.component';

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
      error: (e) => SwalFacade.error("Ocorreu um erro! Não foi possível fazer o logout", e),
      complete: () => this.router.navigate(['/login'])
    });
  }

  /**
   * @Description Abre um modal para visualizar ou cadastrar códigos de acesso
   */
  openAcessCodesModal() {
    this.modalService.open(AcessCodesModalComponent, { size: 'xl' });
  }

  /**
   * @Description Verifica se o usuário possui um grupo específico
   */
  hasGroup(requiredGroup: string): boolean {
    return this.user.user!.groups!.some(group => group.name === requiredGroup);
  }
}
