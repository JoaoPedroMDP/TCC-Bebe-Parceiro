import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Swap } from 'src/app/shared/models/swap';
import { DeleteSwapComponent } from '../delete-swap/delete-swap.component';
import { CreateSwapComponent } from '../create-swap/create-swap.component';
import { EditSwapComponent } from '../edit-swap/edit-swap.component';
import { ApproveRefuseSwapComponent } from '../approve-refuse-swap/approve-refuse-swap.component';

@Component({
  selector: 'app-inspect-swap',
  templateUrl: './inspect-swap.component.html',
  styleUrls: ['./inspect-swap.component.css']
})
export class InspectSwapComponent implements OnInit {

  @Input() swap!: Swap;
isSwapApproved: any;

  constructor(public activeModal: NgbActiveModal, public modalService: NgbModal) { }

  ngOnInit(): void {
  }

  /**
   * Abre o modal de edição para a troca
   */
  editSwap(swap: Swap) {
    this.activeModal.close(); // Fecha o modal atual de visualização
    let modalRef = this.modalService.open(EditSwapComponent, { size: 'xl' })
    modalRef.componentInstance.swap = swap;
    modalRef.componentInstance.editMode = true;
  }

  /**
   * Abre o modal de exclusão para a troca
   */
  deleteSwap(swap: Swap) {
    this.activeModal.close(); // Fecha o modal atual de visualização
    this.modalService.open(DeleteSwapComponent, { size: 'xl' }).componentInstance.swap = swap;
  }

  /**
 * @description Abre um componente modal para aprovar uma troca
 * @param swap O objeto da troca
 */
approveSwap(swap: Swap) {
  this.activeModal.close(); // Fecha o modal atual de visualização
  let modalRef = this.modalService.open(ApproveRefuseSwapComponent, { size: 'xl' });
  modalRef.componentInstance.swap = swap;  // Passando a troca
  modalRef.componentInstance.isApproving = true;        // Passando a flag de aprovação
}

/**
 * @description Abre um componente modal para rejeitar uma troca
 * @param swap O objeto da troca
 */
refuseSwap(swap: Swap) {
  this.activeModal.close(); // Fecha o modal atual de visualização
  let modalRef = this.modalService.open(ApproveRefuseSwapComponent, { size: 'xl' });
  modalRef.componentInstance.swap = swap;  // Passando a troca
  modalRef.componentInstance.isApproving = false;        // Passando a flag de remoção
}

}
