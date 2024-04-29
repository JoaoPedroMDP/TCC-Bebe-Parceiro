import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Beneficiary, SwalFacade } from 'src/app/shared';
import { BeneficiaryService } from '../../services/beneficiary.service';
import { AuthService } from 'src/app/auth';
import { Router } from '@angular/router';

@Component({
  selector: 'app-remove-information',
  templateUrl: './remove-information.component.html',
  styleUrls: ['./remove-information.component.css']
})
export class RemoveInformationComponent implements OnInit {

  @Input() beneficiary!: Beneficiary;
  showSuccess: boolean = false;
  agreeToDelete!: string;

  constructor(public activeModal: NgbActiveModal, private beneficiaryService: BeneficiaryService, private authService: AuthService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  /**
   * @description Verifica se a beneficiada digitou "confirmo" e após isso exclui
   * a beneficiada e faz o logout do usuário
   */
  deleteData() {
    // primeira coisa é fazer um tolowerCase na string para garantir que
    // se o usuário digitar de formas diferentes ainda seja possível excluir
    let confirmChoice = this.agreeToDelete.toLowerCase();
    if (confirmChoice === 'confirmo') {
      this.beneficiaryService.deleteBeneficiary(this.beneficiary.id!).subscribe({
        next: () => {
          // Fecha o Modal e faz o logout
          this.activeModal.close();
          this.authService.logout().subscribe({
            next: () => SwalFacade.success("Usuário desconectado", "Redirecionando ao login"),
            error: (e) => SwalFacade.error("Ocorreu um erro", e),
            complete: () => this.router.navigate(['/login'])
          });
        },
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      })
    } else {
      SwalFacade.alert("Não foi possível excluir, tente novamente", `Você digitou "${this.agreeToDelete}". Para excluir digite apenas "Confirmo"`)
    }
  }
}
