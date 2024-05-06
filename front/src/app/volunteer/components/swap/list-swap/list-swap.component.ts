import { Component, OnDestroy, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { Swap } from 'src/app/shared/models/swap/swap.model';
import { SwapService } from 'src/app/volunteer/services/swap.service';
import { SwalFacade } from 'src/app/shared';

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
      this.listSwaps(); // Atualiza a lista para refletir as mudanças.
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
    
  }
}
