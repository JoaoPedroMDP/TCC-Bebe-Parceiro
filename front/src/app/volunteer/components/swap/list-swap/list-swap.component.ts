import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Swap, SwapPOST } from 'src/app/shared/models/swap';
import { SwapService } from 'src/app/volunteer/services/swap.service';
import { CreateSwapComponent, EditSwapComponent, DeleteSwapComponent, InspectSwapComponent } from '../index';

@Component({
  selector: 'app-list-swap',
  templateUrl: './list-swap.component.html',
  styleUrls: ['./list-swap.component.css']
})
export class ListSwapComponent implements OnInit, OnDestroy {

  swaps!: Swap[];
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private router: Router, private swapService: SwapService) { }

  ngOnInit(): void {
    this.listSwaps(false);
    this.subscription = this.swapService.refreshPage$.subscribe(() => {
      this.listSwaps(false);
    })
  }

  ngOnDestroy(): void {
    this.subscription?.unsubscribe();
  }

  listSwaps(isFiltering: boolean) {
    this.isLoading = true; // Flag de carregamento
    this.swapService.listSwaps().subscribe({
      next: (response) => {
        this.swaps = response;
        // Ordena por descrição de forma segura, verificando por valores nulos ou indefinidos
        this.swaps.sort((a, b) => (a.description ?? '').localeCompare(b.description ?? ''));
      },
      error: (e) => {
        SwalFacade.error("Ocorreu um erro!", e); // Manipula erros
        this.isLoading = false; // Desativa a flag de carregamento em caso de erro
      },
      complete: () => {
        if (isFiltering) {
          // Aplica o filtro apenas se necessário, garantindo que description não seja undefined
          this.swaps = this.swaps.filter(swap => swap.description?.toLowerCase().includes(this.filter.toLowerCase()));
        }
        this.isLoading = false; // Desativa a flag de carregamento após completar a operação
      }
    });
}



  filterSwap(event: Event) {
    if (event != undefined) {
      this.swaps = [];
      if (this.filter != '') {
        this.listSwaps(true);
      } else {
        this.listSwaps(false);
      }
    }
  }

  inspectSwap(swap: Swap) {
    let modalRef = this.modalService.open(InspectSwapComponent, { size: 'xl' });
    modalRef.componentInstance.swap = swap;
  }

  newSwap() {
    let modalRef = this.modalService.open(CreateSwapComponent, { size: 'xl' });
    modalRef.componentInstance.swap = new Swap();
    modalRef.componentInstance.editMode = false;
  }

  editSwap1(swap: Swap) {
    let modalRef = this.modalService.open(EditSwapComponent, { size: 'xl' });
    modalRef.componentInstance.swap = Swap;
    modalRef.componentInstance.editMode = true;
  }

   /**
   * @description Abre o modal de edição
   * @param volunteer objeto do voluntária para ir como variavel no componente
   */
   editSwap(swap: Swap) {
    let swapPOST = new SwapPOST();
    swapPOST.transformObjectToEdit(swap);
    let modalRef = this.modalService.open(EditSwapComponent, { size: 'xl' })
    modalRef.componentInstance.swap = swapPOST;  // Passando o voluntária
    modalRef.componentInstance.editMode = true;          // Passando o modo de edição
    // modalRef.componentInstance.countrySelected = volunteer.city?.state?.country?.id;  // Passando a voluntaria
    // modalRef.componentInstance.stateSelected = volunteer.city?.state?.id;          // Passando o modo de edição
  }

  deleteSwap(swap: Swap) {
    this.modalService.open(DeleteSwapComponent, { size: 'xl' }).componentInstance.swap = swap;
  }
}
