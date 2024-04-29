import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditBeneficiaryComponent } from './edit-beneficiary.component';

describe('EditBeneficiaryComponent', () => {
  let component: EditBeneficiaryComponent;
  let fixture: ComponentFixture<EditBeneficiaryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditBeneficiaryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EditBeneficiaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
