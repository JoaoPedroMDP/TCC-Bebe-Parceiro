import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { firstValueFrom } from 'rxjs';
import { SwalFacade, SwapService } from 'src/app/shared';
import { Beneficiary, Child, Size, SwapPOST, Status } from 'src/app/shared/models';


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
  @Input() statusSelected!: number | undefined; 

  beneficiaries: Beneficiary[] = [];
  children: Child[] = [];
  sizes: Size[] = [];
  shoeSizes!: Size[];
  statuses!: Status[];

  constructor(public activeModal: NgbActiveModal, private swapService: SwapService) {}

  ngOnInit(): void {
    this.loadInitialData();
  }
  
  async loadInitialData() {
    try {
      this.beneficiaries = await firstValueFrom(this.swapService.listBeneficiaries());
      const [sizes, shoeSizes, statuses] = await Promise.all([
        firstValueFrom(this.swapService.listClothSizes()),
        firstValueFrom(this.swapService.listShoeSizes()),
        firstValueFrom(this.swapService.listStatus()),
      ]);
      this.sizes = sizes;
      this.shoeSizes = shoeSizes;
      this.statuses = statuses;
  
      if (this.swap.id) {
        this.fetchSwap(this.swap.id);
      }
    } catch (error) {
      console.error('Failed to load initial data:', error);
    }
  }
  
  async fetchSwap(id: number) {
    try {
      const swap = await firstValueFrom(this.swapService.getSwap(id));
      this.swap.transformObjectToEdit(swap);
      this.statusSelected = this.swap.status_id; 
      this.clothSizeSelected = this.swap.cloth_size_id;
      this.shoeSizeSelected = this.swap.shoe_size_id;

      if (this.swap.beneficiary_id) {
        this.onChangeBeneficiary({ target: { value: this.swap.beneficiary_id.toString() } }, true);
      }
    } catch (error) {
      console.error('Error fetching swap details:', error);
    }
  }
  
  onChangeBeneficiary(event: any, initialLoad: boolean = false) {
    const beneficiaryId = Number(event.target.value);
    this.swap.beneficiary_id = beneficiaryId;
    this.swapService.listChildrenByBeneficiaryId(beneficiaryId).subscribe(
      children => {
        this.children = children;
        if (initialLoad) {
          this.childSelected = this.swap.child_id;
        }
      },
      error => console.error('Failed to load children:', error)
    );
  }

  listChildren(beneficiaryId: number) {
    this.swapService.listChildrenByBeneficiaryId(beneficiaryId).subscribe(
      children => this.children = children,
      error => console.error('Failed to load children:', error)
    );
  }

  listClothSizes() {
    this.swapService.listClothSizes().subscribe({
      next: (response: Size[]) => this.sizes = response,
      error: (e) => SwalFacade.error("Erro ao listar os tamanhos de roupas", e)
    });
  }

  listShoeSizes() {
    this.swapService.listShoeSizes().subscribe({
      next: (response: Size[]) => this.shoeSizes = response,
      error: (e) => SwalFacade.error("Erro ao listar os tamanhos de sapatos", e)
    });
  }

  listStatus() {
    this.swapService.listStatus().subscribe({
      next: (response: Status[]) => this.statuses = response,
      error: (e) => SwalFacade.error("Erro ao listar os status", e)
    });
  }

  save() {
    this.swap.status_id = this.statusSelected;
    this.swap.cloth_size_id = this.clothSizeSelected;
    this.swap.shoe_size_id = this.shoeSizeSelected;
    if (this.form.valid && this.swap && this.swap.id) {
      this.swapService.editSwap(this.swap.id, this.swap).subscribe({
        next: () => SwalFacade.success("Sucesso!", `${this.swap.description} foi atualizado com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e),
        complete: () => this.activeModal.close()
      });
    } else {
      SwalFacade.alert("Formulário inválido!");
    }
  }

  close() {
    this.activeModal.close();
  }
}