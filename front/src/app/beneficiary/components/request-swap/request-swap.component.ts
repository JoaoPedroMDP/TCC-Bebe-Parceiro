import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { BeneficiaryService } from '../../services/beneficiary.service';
import { Child, Size, SwalFacade, SwapPOST } from 'src/app/shared';

@Component({
  selector: 'app-request-swap',
  templateUrl: './request-swap.component.html',
  styleUrls: ['./request-swap.component.css']
})
export class RequestSwapComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  swap!: SwapPOST;
  showSuccess!: boolean;

  children!: Child[];
  sizes!: Size[];
  shoeSizes!: Size[];

  constructor(public activeModal: NgbActiveModal, private beneficiaryService: BeneficiaryService) { }

  ngOnInit(): void {
    this.swap = new SwapPOST();

    this.listChildren();
    this.listClothSizes();
    this.listShoeSizes();
  }

  /**
   * @description Faz um POST salvando o pedido de troca
   */
  requestTrade() {
    if (this.swap.child_id && this.swap.cloth_size_id) {
      this.beneficiaryService.createSwap(this.swap).subscribe({
        next: () => SwalFacade.success("Troca criada com sucesso", `Em breve entraremos em contato`),
        error: (e) => SwalFacade.error("Erro ao salvar!", e),
        complete: () => this.showSuccess = !this.showSuccess
      })
    } else {
      SwalFacade.alert("Não foi possível pedir troca!", "Preencha os campos obrigatórios e tente novamente")
    }
  }

  /**
   * @description Lista as crianças da beneficiada
   */
  listChildren() {
    this.beneficiaryService.listChildren().subscribe({
      next: (response: Child[]) => {
        this.children = response
      },
      error: (e) => SwalFacade.error("Erro ao listar os dados de Tamanhos", e)
    });
  }

  /**
   * @description Lista os tamanhos de roupa
   */
  listClothSizes() {
    this.beneficiaryService.listClothSizes().subscribe({
      next: (response: Size[]) => this.sizes = response,
      error: (e) => SwalFacade.error("Erro ao listar os dados de Tamanhos de Roupas", e)
    });
  }

  /**
   * @description Lista os tamanhos de sapatos
   */
  listShoeSizes() {
    this.beneficiaryService.listShoeSizes().subscribe({
      next: (response: Size[]) => this.shoeSizes = response,
      error: (e) => SwalFacade.error("Erro ao listar os dados de Tamanhos de Sapatos", e)
    });
  }

}
