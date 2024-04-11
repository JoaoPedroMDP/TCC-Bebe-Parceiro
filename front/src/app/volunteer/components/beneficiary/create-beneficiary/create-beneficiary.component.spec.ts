import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateEditBeneficiaryComponent } from './create-beneficiary.component';

describe('CreateEditBeneficiaryComponent', () => {
  let component: CreateEditBeneficiaryComponent;
  let fixture: ComponentFixture<CreateEditBeneficiaryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateEditBeneficiaryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreateEditBeneficiaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
