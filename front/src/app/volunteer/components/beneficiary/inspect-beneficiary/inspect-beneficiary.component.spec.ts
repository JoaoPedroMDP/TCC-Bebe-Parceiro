import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InspectBeneficiaryComponent } from './inspect-beneficiary.component';

describe('InspectBeneficiaryComponent', () => {
  let component: InspectBeneficiaryComponent;
  let fixture: ComponentFixture<InspectBeneficiaryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InspectBeneficiaryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InspectBeneficiaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
