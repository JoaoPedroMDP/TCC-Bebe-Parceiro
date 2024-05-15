import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade } from 'src/app/shared';
import { Swap, SwapPOST } from 'src/app/shared/models/swap';
import { SwapService } from 'src/app/volunteer/services/swap.service';
import { Beneficiary, Child } from 'src/app/shared';
import { Size } from 'src/app/shared/models/swap/size.model';

@Component({
  selector: 'app-create-edit-swap',
  templateUrl: './create-edit-swap.component.html',
  styleUrls: ['./create-edit-swap.component.css']
})
export class CreateEditSwapComponent implements OnInit {

  @Input() swap!: SwapPOST;
  @Input() editMode!: boolean;
  sizes!: Size[];
  beneficiaries!: Beneficiary[];
  children!: Child[];

  constructor(public activeModal: NgbActiveModal, private swapService: SwapService) { }

  ngOnInit(): void {
    this.swap.beneficiary_id;
    this.listBeneficiaries();
    this.listSizes();
  }

  listBeneficiaries() {
    this.swapService.listBeneficiaries().subscribe({
      next: (data: Beneficiary[]) => {
        this.beneficiaries = data || [];
      },
      error: (e) => SwalFacade.error('Erro ao listar os beneficiários', e)
    });
  }

  listSizes() {
    this.swapService.listSizes().subscribe({
      next: (data: Size[]) => {
        if (data == null) {
          this.sizes =  [];
        } else {
          this.sizes = data;
        }
      },
      error: (e) => SwalFacade.error('Erro ao listar os dados de Especialidades', e)
    })
  }

 
  save() {
    if (this.editMode) {
      this.swapService.editSwap(this.swap.id!, this.swap).subscribe({
        next: () => SwalFacade.success("Sucesso!", `Troca atualizada com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      });
    } else {
      this.swapService.createSwap(this.swap).subscribe({
        next: () => SwalFacade.success("Sucesso!", `Troca criada com sucesso!`),
        error: (e) => SwalFacade.error("Ocorreu um erro!", e)
      });
    }
    this.activeModal.close();
  }

  onChangeBeneficiary(event: any) {
    const beneficiaryId = event.target.value as number | undefined;
    if (beneficiaryId !== undefined) {
        this.swap.beneficiary_id = beneficiaryId;
        this.listChildrenByBenefitedId(beneficiaryId);
    } else {
        this.children = [];
    }
}

  listChildrenByBenefitedId(beneficiaryId: number) {
    this.swapService.listChildrenByBenefitedId(beneficiaryId).subscribe({
      next: (children: Child[]) => {
        this.children = children || [];
      },
      error: (e) => SwalFacade.error('Erro ao buscar crianças', e)
    });
  }

  close() {
    this.activeModal.close();
  }
}
