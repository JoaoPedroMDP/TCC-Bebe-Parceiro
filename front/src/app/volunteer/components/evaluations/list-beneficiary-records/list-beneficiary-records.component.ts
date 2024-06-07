import { Component, Input, OnInit } from '@angular/core';
import { EvaluationService } from 'src/app/volunteer/services/evaluation.service';
import { Record, Evaluation} from 'src/app/shared';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-list-beneficiary-records',
  templateUrl: './list-beneficiary-records.component.html',
  styleUrls: ['./list-beneficiary-records.component.css']
})


export class ListBeneficiaryRecordsComponent implements OnInit {
  @Input() beneficiaryId!: number;
  records: Record[] = [];
  evaluation : Evaluation[] = [];
  isLoading = false;
 

  constructor(
    public activeModal: NgbActiveModal,
    private evaluationService: EvaluationService
  ) { }

  ngOnInit(): void {
    this.loadRecords();
   
  }

  loadRecords() {
    this.isLoading = true;
    this.evaluationService.beneficiaryRecords(this.beneficiaryId).subscribe({
      next: (data: Record[]) => {
        this.records = data;
        this.isLoading = false;
      },
      error: (error) => {
        console.error('Error fetching records', error);
        this.isLoading = false;
      }
    });
  }
}