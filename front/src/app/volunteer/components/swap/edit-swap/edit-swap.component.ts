import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';import { catchError } from 'rxjs';
import { SwalFacade, SwapService } from 'src/app/shared';
import { Beneficiary, Child, Size, SwapPOST } from 'src/app/shared/models';

@Component({
  selector: 'app-edit-swap',
  templateUrl: './edit-swap.component.html',
  styleUrls: ['./edit-swap.component.css']
})
export class EditSwapComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  @Input() swap!: SwapPOST;
  @Input() beneficiarySelected!: number;  
  @Input() childSelected!: number | undefined;        
  @Input() clothSizeSelected!: number | undefined;    
  @Input() shoeSizeSelected!: number | undefined;    

  
  beneficiaries: Beneficiary[] = [];
  children: Child[] = [];
  sizes: Size[] = [];
  shoeSizes!: Size[];

  constructor(public activeModal: NgbActiveModal, private swapService: SwapService) {}

  ngOnInit(): void {
    this.swapService.listBeneficiaries().subscribe(beneficiaries => this.beneficiaries = beneficiaries);
    this.swapService.listSizes().subscribe(sizes => this.sizes = sizes);
    if (this.swap.id) {
      this.fetchSwap(this.swap.id);
    }
  }

  fetchSwap(id: number) {
    this.swapService.getSwap(id).subscribe(
      swap => {
        this.swap = swap;
        if (this.swap.beneficiary_id) {
          this.onChangeBeneficiary({ target: { value: this.swap.beneficiary_id.toString() } });
        }
      },
      error => console.error('Error fetching swap details:', error)
    );
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
      },
      error: (e) => SwalFacade.error("Erro ao listar os dados de Tamanhos", e)
    });
  }

  /**
   * @description Lista os tamanhos de roupa
   */
  listClothSizes1() {
    this.swapService.listClothSizes().subscribe({
      next: (response: Size[]) => this.sizes = response,
      error: (e) => SwalFacade.error("Erro ao listar os dados de Tamanhos de Roupas", e)
    });
  }


  listClothSizes() {
    this.swapService.listClothSizes().subscribe({
      next: (data: Size[]) => {
    if (data == null) {
      this.sizes = [];
    } else {
      this.sizes = data;
    }
  }
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

  save() {
    // Verifica se o formulário é válido antes de salvar
    if (this.form.valid && this.swap && this.swap.id) {
      this.swapService.editSwap(this.swap.id, this.swap).subscribe({
        next: () => SwalFacade.success("Sucesso!", `${this.swap.description} foi atualizado com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e),
        complete: () => this.activeModal.close()
      });
    } else {
      SwalFacade.alert("Não foi possível salvar!", "A senhas devem ser iguais!")
    }
  }

 

  validateSwapDetails(): boolean {
    return !!this.swap.beneficiary_id && !!this.swap.child_id && !!this.swap.cloth_size_id && !!this.swap.shoe_size_id;
  }

  close() {
    this.activeModal.close();
  }
}
