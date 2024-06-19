import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { Swap } from 'src/app/shared/models/swap';
import { SwapService } from 'src/app/volunteer/services/swap.service';

@Component({
  selector: 'app-delete-swap',
  templateUrl: './delete-swap.component.html',
  styleUrls: ['./delete-swap.component.css']
})
export class DeleteSwapComponent implements OnInit {

  @Input() swap!: Swap;

  constructor(public activeModal: NgbActiveModal, private swapService: SwapService) { }

  ngOnInit(): void {
  }

  /**
   * @description Executa o método deleteSwap() do swapService e retorna uma mensagem 
   * de sucesso ou erro a depender do resultado da operação.
   */
  deleteSwap() {
    this.swapService.deleteSwap(this.swap.id!).subscribe({
      next: () => SwalFacade.success("Troca excluída", `A troca da beneficiada: ${this.swap.beneficiary?.user?.name} foi excluída com sucesso!`),
      error: (e) => SwalFacade.error("Ocorreu um erro!", `Não foi possível excluir a troca: ${e}`),
      complete: () => this.activeModal.close()
    })
  }
}
