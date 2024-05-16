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

  constructor(public activeModal: NgbActiveModal, private beneficiaryService: BeneficiaryService) { }

  ngOnInit(): void {
    this.swap = new SwapPOST();

    this.listChildren();
    this.listSizes();
  }

  listChildren() {
    this.beneficiaryService.listChildren().subscribe({
      next: (response: Child[]) => this.children = response,
      error: (e) => SwalFacade.error("Erro ao listar os dados de Tamanhos", e)
    });
  }

  listSizes() {
    this.beneficiaryService.listSizes().subscribe({
      next: (response: Size[]) => this.sizes = response,
      error: (e) => SwalFacade.error("Erro ao listar os dados de Tamanhos", e)
    });
  }

  requestTrade() {
    console.log(this.swap);
    
    this.showSuccess = !this.showSuccess
  }
}
