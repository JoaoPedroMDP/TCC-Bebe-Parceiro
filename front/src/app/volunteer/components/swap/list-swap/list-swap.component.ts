import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Swap, SwapPOST } from 'src/app/shared/models/swap';
import { SwapService } from 'src/app/volunteer/services/swap.service';
import { CreateSwapComponent, EditSwapComponent, DeleteSwapComponent, InspectSwapComponent } from '../index';
import { Status } from 'src/app/shared/models/swap/status.model';
@Component({
  selector: 'app-list-swap',
  templateUrl: './list-swap.component.html',
  styleUrls: ['./list-swap.component.css']
})
export class ListSwapComponent implements OnInit, OnDestroy {

  swaps!: Swap[];
  originalSwaps!: Swap[];  // Armazena os swaps originais para aplicar filtros
  filter!: string;
  selectedStatus!: string;  // Armazena o status selecionado
  isLoading: boolean = false;
  subscription: Subscription | undefined;
  statuses!: Status[];
  

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
        this.originalSwaps = response; // Armazena os swaps originais para filtragem
          this.filterSwap();
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

filterSwap() {
  if (this.filter) {
    const filterLower = this.filter.toLowerCase();
    this.swaps = this.originalSwaps.filter(swap =>
      (swap.description?.toLowerCase().includes(filterLower) ||
       swap.beneficiary?.user?.name?.toLowerCase().includes(filterLower) ||
       swap.cloth_size?.name?.toLowerCase().includes(filterLower) ||
       swap.shoe_size?.name?.toLowerCase().includes(filterLower) ||
       swap.status?.name?.toLowerCase().includes(filterLower))
    );
  } else {
    this.swaps = [...this.originalSwaps]; // Retorna todos os swaps se não há filtro
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

   editSwap(swap: Swap) {
    let swapPOST = new SwapPOST();
    swapPOST.transformObjectToEdit(swap);
    let modalRef = this.modalService.open(EditSwapComponent, { size: 'xl' })
    modalRef.componentInstance.swap = swapPOST;  
    modalRef.componentInstance.editMode = true;        

  }

  deleteSwap(swap: Swap) {
    this.modalService.open(DeleteSwapComponent, { size: 'xl' }).componentInstance.swap = swap;
  }
}
