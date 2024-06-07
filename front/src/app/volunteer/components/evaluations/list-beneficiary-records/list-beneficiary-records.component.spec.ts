import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListBeneficiaryRecordsComponent } from './list-beneficiary-records.component';

describe('ListBeneficiaryRecordsComponent', () => {
  let component: ListBeneficiaryRecordsComponent;
  let fixture: ComponentFixture<ListBeneficiaryRecordsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListBeneficiaryRecordsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListBeneficiaryRecordsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
