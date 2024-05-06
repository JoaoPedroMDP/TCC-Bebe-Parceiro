import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { SwapService } from 'src/app/volunteer/services/swap.service';

@Component({
  selector: 'app-create-edit-swap',
  templateUrl: './create-edit-swap.component.html',
  styleUrls: ['./create-edit-swap.component.css']
})
export class CreateEditSwapComponent implements OnInit {
  @Input() swap: any;  // Substituir 'any' pelo modelo apropriado
  @Input() editMode!: boolean;

  constructor(
    public activeModal: NgbActiveModal,
    private swapService: SwapService // Injeta o serviço de swaps
  ) { }

  ngOnInit(): void {
  }

  /**
   * @description Salva ou atualiza os dados da troca dependendo do modo de edição
   */
  save() {
    if (this.editMode) {
      // Atualiza a troca existente
      this.swapService.editSwap(this.swap.id, this.swap).subscribe({
        next: () => {
          SwalFacade.success("Sucesso!", `${this.swap.name} foi atualizada com sucesso!`);
          this.activeModal.close();
        },
        error: (e) => {
          SwalFacade.error("Erro ao atualizar!", e);
        }
      });
    } else {
      // Cria uma nova troca
      this.swapService.createSwap(this.swap).subscribe({
        next: () => {
          SwalFacade.success("Sucesso!", `${this.swap.name} foi criada com sucesso!`);
          this.activeModal.close();
        },
        error: (e) => {
          SwalFacade.error("Erro ao criar!", e);
        }
      });
    }
  }

  /**
   * @description Deleta a troca
   */
  deleteSwap() {
    this.swapService.deleteSwap(this.swap.id).subscribe({
      next: () => {
        SwalFacade.success("Deletado!", `${this.swap.name} foi deletada com sucesso!`);
        this.activeModal.close();
      },
      error: (e) => {
        SwalFacade.error("Erro ao deletar!", e);
      }
    });
  }

  /**
   * @description Fecha o modal
   */
  close() {
    this.activeModal.close();
  }
}
