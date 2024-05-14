import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { SwapService } from 'src/app/volunteer/services/swap.service'; 
import { Swap } from 'src/app/shared/models/swap/swap.model';

@Component({
  selector: 'app-delete-swap',
  templateUrl: './delete-swap.component.html',
  styleUrls: ['./delete-swap.component.css']
})
export class DeleteSwapComponent implements OnInit {

  @Input() swap!: Swap;

  constructor(
    public activeModal: NgbActiveModal, 
    private swapService: SwapService
  ) { }

  ngOnInit(): void {
  }

  /**
   * @description Executes the deleteSwap() method from the swapService and returns a success or error message 
   * depending on the operation result
   */
  deleteSwap() {
    this.swapService.deleteSwap(this.swap.id!).subscribe({
      next: () => {
        SwalFacade.success("Troca Excluída", `${this.swap.beneficiaryName}'s swap foi excluída com sucesso!`);
        this.activeModal.close();
      },
      error: (e) => SwalFacade.error("Erro ao excluir!", `Não foi possível excluir a troca: ${e}`)
    });
  }
}

