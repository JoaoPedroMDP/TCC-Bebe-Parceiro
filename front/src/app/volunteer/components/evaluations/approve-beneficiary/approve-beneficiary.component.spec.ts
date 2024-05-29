import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ApproveBeneficiaryComponent } from './approve-beneficiary.component';

describe('ApproveBeneficiaryComponent', () => {
  let component: ApproveBeneficiaryComponent;
  let fixture: ComponentFixture<ApproveBeneficiaryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ApproveBeneficiaryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ApproveBeneficiaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
