import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Swap } from 'src/app/shared/models/swap/swap.model';
import { CreateEditSwapComponent } from '../create-edit-swap/create-edit-swap.component';
import { DeleteSwapComponent } from '../delete-swap/delete-swap.component'; // Asumindo que você tenha um componente para deletar

@Component({
  selector: 'app-inspect-swap',
  templateUrl: './inspect-swap.component.html',
  styleUrls: ['./inspect-swap.component.css']
})
export class InspectSwapComponent implements OnInit {

  @Input() swap!: Swap;

  constructor(
    public activeModal: NgbActiveModal,
    private modalService: NgbModal
  ) { }

  ngOnInit(): void {
  }

  /**
   * Abre o modal de edição para a troca atual.
   */
  editSwap() {
    this.activeModal.close(); // Fecha o modal de inspeção antes de abrir o de edição
    const modalRef = this.modalService.open(CreateEditSwapComponent, { size: 'lg' });
    modalRef.componentInstance.swap = this.swap; // Passa a troca atual para o componente de edição
  }

  /**
   * Abre o modal de exclusão para a troca atual.
   */
  deleteSwap() {
    this.activeModal.close(); // Fecha o modal de inspeção antes de abrir o de exclusão
    const modalRef = this.modalService.open(DeleteSwapComponent, { size: 'lg' });
    modalRef.componentInstance.swap = this.swap; // Passa a troca atual para o componente de exclusão
  }

  /**
   * Fecha o modal atual.
   */
  close() {
    this.activeModal.close();
  }
}
