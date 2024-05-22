import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade, SwapService } from 'src/app/shared';
import { Child, Size, Status, SwapPOST } from 'src/app/shared/models';


@Component({
  selector: 'app-edit-swap',
  templateUrl: './edit-swap.component.html',
  styleUrls: ['./edit-swap.component.css']
})
export class EditSwapComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  @Input() swap!: SwapPOST;
  @Input() beneficiaryName!: string;

  children: Child[] = [];
  clothSizes: Size[] = [];
  shoeSizes!: Size[];
  isSwapApproved!: boolean;
  statuses!: Status[];

  constructor(public activeModal: NgbActiveModal, private swapService: SwapService) { }

  ngOnInit(): void {
    this.listClothSizes();
    this.listShoeSizes();
    this.listChildren();
    this.listStatuses();
  }

  /**
   * @description Edita uma troca existente
   */
  save() {
    if (this.swap.id) {
      this.swapService.editSwap(this.swap.id, this.swap).subscribe({
        next: () => SwalFacade.success("Sucesso!", `A troca da beneficiada: ${this.beneficiaryName} foi atualizada com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e),
        complete: () => this.activeModal.close()
      });
    } else {
      SwalFacade.alert("Formulário inválido!");
    }
  }

  /**
   * @description Lista as crianças da beneficiada
   */
  listChildren() {
    this.swapService.listChildrenByBeneficiaryId(this.swap.beneficiary_id!).subscribe({
      next: (response: Child[]) => this.children = response,
      error: (e) => SwalFacade.error("Erro ao listar as crianças da beneficiada", e)
    });
  }

  /**
   * @description Lista os tamanhos de roupa
   */
  listClothSizes() {
    this.swapService.listClothSizes().subscribe({
      next: (response: Size[]) => this.clothSizes = response,
      error: (e) => SwalFacade.error("Erro ao listar os dados de Tamanhos de Roupas", e)
    });
  }

  /**
   * @description Lista os tamanhos de sapatos
   */
  listShoeSizes() {
    this.swapService.listShoeSizes().subscribe({
      next: (response: Size[]) => this.shoeSizes = response,
      error: (e) => SwalFacade.error("Erro ao listar os dados de Tamanhos de Sapatos", e)
    });
  }

  /**
   * @description Fecha o modal
   */
  close() {
    this.activeModal.close();
    this.swapService.refreshPage$.next();
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
        // Define o status da troca como aprovado
        this.swap.status_id = aprovadoId;
        this.swapService.editSwap(this.swap.id!, this.swap).subscribe({
          next: () => SwalFacade.success("Troca aprovada com sucesso!", `Troca de ${this.beneficiaryName} foi aprovada!`),
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
      next: () => SwalFacade.success("Troca removida com sucesso!", `Troca de ${this.beneficiaryName} foi removida!`),
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
        // Define o status da troca como encerrado
        this.swap.status_id = encerradoId;
        this.swapService.editSwap(this.swap.id!, this.swap).subscribe({
          next: () => SwalFacade.success("Troca encerrada com sucesso!", `Troca de ${this.beneficiaryName}} foi encerrada!`),
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
        // Define o status da troca como cancelado
        this.swap.status_id = canceladoId;
        this.swapService.editSwap(this.swap.id!, this.swap).subscribe({
          next: () => SwalFacade.success("Troca cancelada com sucesso!", `Troca de ${this.beneficiaryName}} foi cancelada!`),
          error: (e) => SwalFacade.error("Ocorreu um erro!", e),
          complete: () => this.activeModal.close()
        });
      }
    })
  }
}
