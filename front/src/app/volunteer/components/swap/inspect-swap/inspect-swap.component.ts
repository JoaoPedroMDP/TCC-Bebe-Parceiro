import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Status, Swap, SwapPOST } from 'src/app/shared/models/swap';
import { DeleteSwapComponent } from '../delete-swap/delete-swap.component';
import { EditSwapComponent } from '../edit-swap/edit-swap.component';
import { SwalFacade, SwapService } from 'src/app/shared';

@Component({
  selector: 'app-inspect-swap',
  templateUrl: './inspect-swap.component.html',
  styleUrls: ['./inspect-swap.component.css']
})
export class InspectSwapComponent implements OnInit {

  @Input() swap!: Swap;
  @Input() isSwapApproved!: boolean;
  @Input() isSwapClosed!: boolean;

  statuses!: Status[];

  constructor(public activeModal: NgbActiveModal, public modalService: NgbModal, private swapService: SwapService) { }

  ngOnInit(): void {
    this.listStatuses();
  }

  /**
   * @description Abre o modal de edição para a troca
   */
  editSwap() {
    this.activeModal.close(); // Fecha o modal atual de visualização

    let swapPOST = new SwapPOST();
    swapPOST.transformObjectToEdit(this.swap);

    let modalRef = this.modalService.open(EditSwapComponent, { size: 'xl' })
    modalRef.componentInstance.swap = swapPOST;
    modalRef.componentInstance.beneficiaryName = this.swap.beneficiary?.user?.name;
    modalRef.componentInstance.isSwapApproved = this.isSwapApproved;
  }

  /**
   * @description Abre o modal de exclusão para a troca
   */
  deleteSwap() {
    this.activeModal.close(); // Fecha o modal atual de visualização
    this.modalService.open(DeleteSwapComponent, { size: 'xl' }).componentInstance.swap = this.swap;
  }

  /**
   * @description Lista os status do sistema - método MUITO IMPORTANTE pois todos os métodos que alteram
   * o status da troca precisam pesquisar através do array statuses para fazer alguma mudança
   */
  listStatuses() {
    this.swapService.listStatuses().subscribe({
      next: (response: Status[]) => this.statuses = response,
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => console.log(this.statuses)
    })
  }

  /**
   * @description Encontra o ID de um status filtrando o array this.statuses para procurar um valor
   * @param name O valor a ser procurado
   * @returns o ID do status caso encontrado ou undefined caso não encontrado
   */
  findStatusIdByName(name: string): number | undefined {
    const status = this.statuses.find(status => status.name === name);
    return status?.id;
  }

  /**
   * @description Primeiro procura o id do status que contém o nome de "Aprovado", então joga o valor desse id
   * para o objeto swap e executa um PATCH assim mudando o status da troca para aprovada
   */
  approveSwap() {
    SwalFacade.approve("Aprovar a troca", "Aprovar", "Você tem certeza da sua opção?").then((result) => {
      if (result.isConfirmed) {
        const aprovadoId = this.findStatusIdByName("Aprovado");
        let swapPOST = new SwapPOST();
        swapPOST.transformObjectToEdit(this.swap);
        // Define o status da troca como aprovado
        swapPOST.status_id = aprovadoId;
        this.swapService.editSwap(swapPOST.id!, swapPOST).subscribe({
          next: () => SwalFacade.success("Troca aprovada com sucesso!", `Troca de ${this.swap.beneficiary?.user?.name} foi aprovada!`),
          error: (e) => SwalFacade.error("Ocorreu um erro!", e),
          complete: () => this.activeModal.close()
        });
      }
    })
  }

  /**
   * @description Recusa uma troca - simplesmente envia um DELETE e remove a troca
   */
  refuseSwap() {
    this.swapService.deleteSwap(this.swap.id!).subscribe({
      next: () => SwalFacade.success("Troca removida com sucesso!", `Troca de ${this.swap.beneficiary?.user?.name} foi removida!`),
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.activeModal.close()
    });
  }

  /**
   * @description Primeiro procura o id do status que contém o nome de "Encerrado", então joga o valor desse id
   * para o objeto swap e executa um PATCH assim mudando o status da troca para encerrada
   */
  finishSwap() {
    SwalFacade.approve("Encerrar a troca", "Encerrar", "Você tem certeza da sua opção?").then((result) => {
      if (result.isConfirmed) {
        const encerradoId = this.findStatusIdByName("Encerrado");
        let swapPOST = new SwapPOST();
        swapPOST.transformObjectToEdit(this.swap);
        // Define o status da troca como encerrado
        swapPOST.status_id = encerradoId;
        this.swapService.editSwap(swapPOST.id!, swapPOST).subscribe({
          next: () => SwalFacade.success("Troca encerrada com sucesso!", `Troca de ${this.swap.beneficiary?.user?.name}} foi encerrada!`),
          error: (e) => SwalFacade.error("Ocorreu um erro!", e),
          complete: () => this.activeModal.close()
        });
      }
    })
  }

  /**
   * @description Primeiro procura o id do status que contém o nome de "Cancelado", então joga o valor desse id
   * para o objeto swap e executa um PATCH assim mudando o status da troca para cancelada
   */
  cancelSwap() {
    SwalFacade.delete("Cancelar a troca", "Cancelar", "Você tem certeza da sua opção?").then((result) => {
      if (result.isConfirmed) {
        const canceladoId = this.findStatusIdByName("Cancelado");
        let swapPOST = new SwapPOST();
        swapPOST.transformObjectToEdit(this.swap);
        // Define o status da troca como cancelado
        swapPOST.status_id = canceladoId;
        this.swapService.editSwap(swapPOST.id!, swapPOST).subscribe({
          next: () => SwalFacade.success("Troca cancelada com sucesso!", `Troca de ${this.swap.beneficiary?.user?.name}} foi cancelada!`),
          error: (e) => SwalFacade.error("Ocorreu um erro!", e),
          complete: () => this.activeModal.close()
        });
      }
    })
  }
}
