import { Component, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade, SwapService, VolunteerService } from 'src/app/shared';
import { Beneficiary, Child, Size, SwapPOST } from 'src/app/shared/models';

@Component({
  selector: 'app-create-swap',
  templateUrl: './create-swap.component.html',
  styleUrls: ['./create-swap.component.css']
})
export class CreateSwapComponent implements OnInit {

  swap!: SwapPOST;
  beneficiaries!: Beneficiary[];
  children!: Child[];
  clothSizes!: Size[];
  shoeSizes!: Size[];

  constructor(public activeModal: NgbActiveModal, private swapService: SwapService, private volunteerService: VolunteerService) { }

  ngOnInit(): void {
    this.swap = new SwapPOST(); // Inicializa um objeto de troca
    this.listBeneficiaries();
    this.listClothSizes();
    this.listShoeSizes();
  }

  /**
   * @description Salva uma nova troca
   */
  save() {
    this.swapService.createSwap(this.swap).subscribe({
      next: () => SwalFacade.success("Sucesso!", `Troca criada com sucesso!`),
      error: (e) => SwalFacade.error("Erro ao salvar!", e),
      complete: () => this.activeModal.close(),
    });
  }

  /**
   * @description Lista as beneficiadas
   */
  listBeneficiaries() {
    this.volunteerService.listBeneficiary().subscribe({
      next: (response: Beneficiary[]) => this.beneficiaries = response,
      error: (e) => SwalFacade.error("Erro ao listar as beneficiadas", e)
    });
  }

  /**
   * @description Lista as crianças da beneficiada
   * @param event o Id da beneficiada que irá filtrar as crianças
   */
  listChildren(event: any) {
    const beneficiaryId = Number(event.target.value);
    // Lista as crianças já filtradas através do id da beneficiada
    if (beneficiaryId) {
      this.swapService.listChildrenByBeneficiaryId(beneficiaryId).subscribe({
        next: (response: Child[]) => this.children = response,
        error: (e) => SwalFacade.error("Erro ao listar as crianças da beneficiada", e)
      });
    } else {
      this.children = []; // Limpa o array das crianças se nenhuma beneficiada for selecionada
    }
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
   * @description Lista os tamanhos de roupa
   */
  listClothSizes() {
    this.swapService.listClothSizes().subscribe({
      next: (response: Size[]) => this.clothSizes = response,
      error: (e) => SwalFacade.error("Erro ao listar os dados de Tamanhos de Roupas", e)
    });
  }

  /**
   * @description Fecha o modal
   */
  close() {
    this.activeModal.close();
    this.swapService.refreshPage$.next();
  }
}


