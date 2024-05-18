import { Component, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade, SwapService } from 'src/app/shared';
import { Beneficiary, Child, Size, SwapPOST } from 'src/app/shared/models';

@Component({
  selector: 'app-create-swap',
  templateUrl: './create-swap.component.html',
  styleUrls: ['./create-swap.component.css']
})
export class CreateSwapComponent implements OnInit {
  swap: SwapPOST = new SwapPOST();
  beneficiaries: Beneficiary[] = [];
  children: Child[] = [];
  sizes: Size[] = [];

  constructor(public activeModal: NgbActiveModal, private swapService: SwapService) { }

  ngOnInit(): void {
    this.swapService.listBeneficiaries().subscribe(beneficiaries => this.beneficiaries = beneficiaries);
    this.swapService.listSizes().subscribe(sizes => this.sizes = sizes);
    this.listChildren();
  }

  onChangeBeneficiary(event: any) {
    const beneficiaryId = Number(event.target.value);
    this.swap.beneficiary_id = beneficiaryId;
    if (beneficiaryId) {
      this.swapService.listChildrenByBeneficiaryId(beneficiaryId).subscribe(
        children => this.children = children,
        error => console.error('Failed to load children:', error)
      );
    } else {
      this.children = []; // Clear children if no valid beneficiary is selected
    }
  }


 /**
   * @description Lista as crianças da beneficiada
   */
 listChildren() {
  this.swapService.listChildren().subscribe({
    next: (response: Child[]) => {
      this.children = response
      console.log(this.children)
    },
    error: (e) => SwalFacade.error("Erro ao listar os dados de Tamanhos", e)
  });
}

  save() {
    this.swapService.createSwap(this.swap).subscribe({
      next: () => {
        this.activeModal.close();
        alert('Troca criada com sucesso!');
      },
      error: (e) => alert(`Erro ao criar troca: ${e.message}`)
    });
  }
    /**
   * @description Fecha o modal
   */
    close() {
      this.activeModal.close();
    }
}


