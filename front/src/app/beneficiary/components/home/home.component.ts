import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { AuthService } from 'src/app/auth';
import { SwalFacade, UserToken } from 'src/app/shared';
import { RequestSwapComponent } from '../request-swap/request-swap.component';
import { BeneficiaryService } from '../../services/beneficiary.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  user!: UserToken;
  canSwap: boolean = true;

  constructor(private authService: AuthService, private router: Router, private modalService: NgbModal,
    private beneficiaryService: BeneficiaryService,) { }

  ngOnInit(): void {
    this.user = this.authService.getUser();
    // Verifica se a beneficiada pode realizar trocas
    this.beneficiaryService.isBeneficiaryAbleToSwap().subscribe({
      next: (response) => this.canSwap = response.can_request_swap
    });
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
    if (this.canSwap) {
      this.modalService.open(RequestSwapComponent, { size: 'xl' });
    } else{
      SwalFacade.alert("Não foi possível pedir uma troca", "Você já tem uma troca em aberto!")
    }
  }
}
