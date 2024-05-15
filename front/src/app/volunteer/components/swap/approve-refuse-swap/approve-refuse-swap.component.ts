import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { Swap, SwapPOST } from 'src/app/shared/models/swap';
import { Status } from 'src/app/shared/models/swap/status.model';
import { SwapService } from 'src/app/volunteer/services/swap.service';

@Component({
  selector: 'app-approve-refuse-swap',
  templateUrl: './approve-refuse-swap.component.html',
  styleUrls: ['./approve-refuse-swap.component.css']
})
export class ApproveRefuseSwapComponent implements OnInit {

  @Input() swap!: SwapPOST;
  @Input() isApproving!: boolean;

  constructor(public activeModal: NgbActiveModal, private swapService: SwapService) { }

  ngOnInit(): void {
  }

  /**
   * @description Altera o status da troca para aprovado e chama o método editSwap() do service
   */
  approveSwap() {
    // Define o status da troca como aprovado
    // VERIFICAR
    this.swapService.editSwap(this.swap.id!, this.swap).subscribe({
      next: () => SwalFacade.success("Troca aprovada com sucesso!", `Troca de ${this.swap.description} foi aprovada!`),
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.activeModal.close()
    });
  }

  /**
   * @description Chama o método deleteSwap() do service para remover a troca
   */
  refuseSwap() {
    this.swapService.deleteSwap(this.swap.id!).subscribe({
      next: () => SwalFacade.success("Troca removida com sucesso!", `Troca de ${this.swap.description} foi removida!`),
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.activeModal.close()
    });
  }
}
