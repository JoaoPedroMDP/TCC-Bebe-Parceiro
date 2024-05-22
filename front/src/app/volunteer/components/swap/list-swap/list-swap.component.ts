import { Component, OnDestroy, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade, SwapService } from 'src/app/shared';
import { Swap, SwapPOST } from 'src/app/shared/models/swap';
import { CreateSwapComponent, DeleteSwapComponent, EditSwapComponent, InspectSwapComponent } from '../index';


@Component({
  selector: 'app-list-swap',
  templateUrl: './list-swap.component.html',
  styleUrls: ['./list-swap.component.css']
})
export class ListSwapComponent implements OnInit, OnDestroy {

  swaps!: Swap[];
  originalSwaps!: Swap[];  // Armazena as trocas originais para aplicar filtros
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private swapService: SwapService) { }

  ngOnInit(): void {
    this.listSwaps();  // Lista inicialmente as trocas
    this.subscription = this.swapService.refreshPage$.subscribe(() => {
      this.listSwaps(); // Lista as trocas novamente para refletir as atualizações.
    })
  }

  ngOnDestroy(): void {
    // Cancela a subscrição para evitar vazamentos de memória.
    this.subscription?.unsubscribe();
  }

  /**
   * @description lista os dados de trocas
   */
  listSwaps() {
    this.isLoading = true; // Flag de carregamento
    this.swapService.listSwaps().subscribe({
      next: (response) => {
        this.originalSwaps = response; // Armazena os swaps originais para filtragem
        this.filterSwap(); // Chama o componente de filtragem inicialmente
      },
      error: (e) => {
        SwalFacade.error("Ocorreu um erro!", e); // Manipula erros
        this.isLoading = false; // Desativa a flag de carregamento em caso de erro
      },
      complete: () => this.isLoading = false
    });
  }

  /**
   * @description Filtra os campos de nome, tamanho da roupa e status pelo input inserido
   */
  filterSwap() {
    if (this.filter) {
      const filterLower = this.filter.toLowerCase();
      this.swaps = this.originalSwaps.filter(swap => (
        swap.beneficiary?.user?.name?.toLowerCase().includes(filterLower) ||
        swap.cloth_size?.name?.toLowerCase().includes(filterLower) ||
        swap.status?.name?.toLowerCase().includes(filterLower))
      );
    } else {
      this.swaps = [...this.originalSwaps]; // Retorna todos os swaps se não há filtro
    }
  }

  /**
   * @description Abre o modal de inspeção
   * @param swap objeto da troca para ir como variavel no componente
   */
  inspectSwap(swap: Swap) {
    let isSwapApproved = swap.status?.name == "Pendente" ? false : true;
    let isSwapClosed = swap.status?.name == "Encerrado" || swap.status?.name == "Cancelado" ? true : false;
    let modalRef = this.modalService.open(InspectSwapComponent, { size: 'xl' })
    modalRef.componentInstance.swap = swap;
    modalRef.componentInstance.isSwapApproved = isSwapApproved;
    modalRef.componentInstance.isSwapClosed = isSwapClosed;
  }

  /**
   * @description Abre o modal de criação
   */
  newSwap() {
    this.modalService.open(CreateSwapComponent, { size: 'xl' });
  }

  /**
   * @description Cria um objeto SwapPOST e transforma o parametro swap para poder fazer a edição
   * Após isso abre o modal de edição e passa parametros adicionais
   * @param swap objeto da troca para ir como variavel no componente
   */
  editSwap(swap: Swap) {
    let swapPOST = new SwapPOST();
    let isSwapApproved = swap.status?.name == "Pendente" ? false : true;
    swapPOST.transformObjectToEdit(swap);
    let modalRef = this.modalService.open(EditSwapComponent, { size: 'xl' })
    modalRef.componentInstance.swap = swapPOST;
    modalRef.componentInstance.beneficiaryName = swap.beneficiary?.user?.name;
    modalRef.componentInstance.isSwapApproved = isSwapApproved;
  }

  /**
   * @description Abre o modal de exclusão
   * @param swap objeto da troca para ir como variavel no componente
   */
  deleteSwap(swap: Swap) {
    this.modalService.open(DeleteSwapComponent, { size: 'xl' }).componentInstance.swap = swap;
  }
}
