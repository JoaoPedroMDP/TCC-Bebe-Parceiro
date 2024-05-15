import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Swap } from 'src/app/shared/models/swap';
import { DeleteSwapComponent } from '../delete-swap/delete-swap.component';
import { CreateEditSwapComponent } from '../create-edit-swap/create-edit-swap.component';

@Component({
  selector: 'app-inspect-swap',
  templateUrl: './inspect-swap.component.html',
  styleUrls: ['./inspect-swap.component.css']
})
export class InspectSwapComponent implements OnInit {

  @Input() swap!: Swap;

  constructor(public activeModal: NgbActiveModal, public modalService: NgbModal) { }

  ngOnInit(): void {
  }

  /**
   * Abre o modal de edição para a troca
   */
  editSwap(swap: Swap) {
    this.activeModal.close(); // Fecha o modal atual de visualização
    let modalRef = this.modalService.open(CreateEditSwapComponent, { size: 'xl' })
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
}
