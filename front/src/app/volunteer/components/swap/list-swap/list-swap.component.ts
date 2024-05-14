import { Component, OnDestroy, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Swap } from 'src/app/shared/models/swap/swap.model';
import { SwapService } from 'src/app/shared';
import { CreateEditSwapComponent, DeleteSwapComponent, InspectSwapComponent } from '../index';

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

  constructor(private modalService: NgbModal, private swapService: SwapService) { }

  ngOnInit(): void {
    this.listSwaps();
    this.subscription = this.swapService.refreshPage$.subscribe(() => {
      this.listSwaps();
    });
  }

  ngOnDestroy(): void {
    this.subscription?.unsubscribe();
  }

  listSwaps() {
    this.isLoading = true;
    this.swapService.listSwaps().subscribe({
      next: (response) => {
        this.swaps = response;
        this.swaps.sort((a, b) => a.beneficiaryName.localeCompare(b.beneficiaryName));
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => this.isLoading = false
    });
  }

  filterSwaps(event: Event) {
    if (event !== undefined && this.filter !== '') {
      this.swaps = this.swaps.filter(swap => swap.beneficiaryName.toLowerCase().includes(this.filter.toLowerCase()));
    } else {
      this.listSwaps();
    }
  }

  inspectSwap(swap: Swap) {
    let modalRef = this.modalService.open(InspectSwapComponent, { size: 'xl' });
    modalRef.componentInstance.swap = swap;
  }

  newSwap() {
    let modalRef = this.modalService.open(CreateEditSwapComponent, { size: 'xl' });
    modalRef.componentInstance.swap = new Swap('', '', '', ''); // Adjust with appropriate defaults or create a method to initialize
    modalRef.componentInstance.editMode = false;
  }

  editSwap(swap: Swap) {
    let modalRef = this.modalService.open(CreateEditSwapComponent, { size: 'xl' });
    modalRef.componentInstance.swap = swap;
    modalRef.componentInstance.editMode = true;
  }

  deleteSwap(swap: Swap) {
    let modalRef = this.modalService.open(DeleteSwapComponent, { size: 'xl' });
    modalRef.componentInstance.swap = swap;
  }
}
